(N, M) = map(int, input().split())
A = [int(c) for c in input().split()]
A.sort(reverse=True)
B = A[::-1]
l = 0
r = 10 ** 6


def f(m):
    cnt = 0
    j = 0
    for i in range(N):
        while j < N:
            if A[i] + B[j] >= m:
                cnt += N - j
                break
            j += 1
    return cnt >= M


while l + 1 < r:
    n = (l + r) // 2
    if f(n):
        l = n
    else:
        r = n
C = [0]
for i in range(N):
    C += [C[-1] + B[i]]
ans = 0
j = 0
m = 0
flag = False
for i in range(N):
    while j < N:
        if A[i] + B[j] > l:
            ans += C[-1] - C[j] + A[i] * (N - j)
            m += N - j
            break
        j += 1
ans += (M - m) * l
print(ans)
