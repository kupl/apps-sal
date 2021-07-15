from bisect import bisect_left


def solve(m):
    r = N - 1
    l = 0
    cnt = 0
    while 0 <= r and l < N:
        if A[r] + A[l] < m:
            l += 1
        else:
            cnt += N - l
            r -= 1
    return cnt


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

# [ok, ng) - Maximum
# (ng, ok] - Minimum
# ok が 最終的な答え
ok = 0
ng = 10 ** 21
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    cnt = solve(mid)
    if cnt >= M:
        ok = mid
    else:
        ng = mid

X = ok
amari = float('inf')
cnt = 0
score = 0
for i, Ai in enumerate(A):
    Aj = X - Ai
    j = bisect_left(A, Aj)
    score += S[N] - S[j] + Ai * (N - j)
    cnt += N - j
    if j < N:
        amari = min(amari, A[i] + A[j])

print((score - (cnt - M) * amari))

