import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None] * T
inf = 10 ** 9 + 7
for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))
    bj = A.count(1)
    sj = 2 * N - bj
    x = sj - bj
    A1 = [3 - 2 * a for a in A[:N][::-1]]
    A2 = [3 - 2 * a for a in A[N:]]
    for i in range(1, N):
        A1[i] += A1[i - 1]
        A2[i] += A2[i - 1]
    geta = -min(0, min(A2)) + 1
    mA = max(0, max(A2))
    idx = [inf] * (mA + geta + 1)
    idx[geta + 0] = 0
    for i in range(N):
        a2 = A2[i]
        idx[geta + a2] = min(idx[geta + a2], i + 1)
    ans = inf
    A1 = [0] + A1
    for i in range(N + 1):
        a1 = A1[i]
        if -geta <= -a1 - x <= mA:
            ans = min(ans, i + idx[geta - a1 - x])
    Ans[qu] = ans
print('\n'.join(map(str, Ans)))
