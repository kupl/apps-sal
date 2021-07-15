import bisect
def judge(k, N, A):
    t = 0
    for i in A:
        j = bisect.bisect_left(A, k - i)
        t += N - j
    return t
def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    t = A[-1] * 2
    b = 0
    X = None
    while t - b > 1:
        m = (t + b)//2
        i = judge(m, N, A)
        if i == M:
            X = m
            break
        if i > M:
            ip = judge(m + 1, N, A)
            if ip == M:
                X = m + 1
                break
            if ip < M:
                X = m
                break
            b = m + 1
        if i < M:
            im = judge(m - 1, N, A)
            if im >= M:
                X = m - 1
                break
            t = m - 1
    if X is None:
        X = b
    B = []
    tmp = 0
    for i in reversed(list(range(N))):
        tmp += A[i]
        B.append(tmp)
    B.reverse()
    r = 0
    tot = 0
    for i in reversed(list(range(N))):
        j = bisect.bisect_left(A, X - A[i])
        tot += N - j
        if j == N:
            break
        r += A[i] * (N - j) + B[j]
    return r - (tot - M) * X
print((main()))

