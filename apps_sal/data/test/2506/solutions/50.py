def judge(k, N, A):
    p = N - 1
    t = 0
    for i in A:
        while p >= 0 and A[p] + i < k:
            p -= 1
        t += (p + 1)
    return t
def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    t = A[0] * 2
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
    r = 0
    p = N - 1
    k = sum(A)
    for i in A:
        while p >= 0 and A[p] + i < X :
            k -= A[p]
            p -= 1
        r += i * (p + 1) + k
    return r - (judge(X, N, A) - M) * X
print((main()))

