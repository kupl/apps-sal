import sys
from bisect import bisect_right


def solve(t):
    nonlocal A, B, C
    k = bisect_right(H, B * t)
    cnt = 0
    for i in range(k, N):
        h = H[i]
        h -= B * t
        cnt += (h + C - 1) // C
    return cnt <= t


N, A, B = list(map(int, input().split()))
C = A - B
H = [int(s) for s in sys.stdin.readlines()]

H.sort()

# [ok, ng) - Maximum
# (ng, ok] - Minimum
# ok が 最終的な答え
ng = 0
ok = 10 ** 9 + 1000
k = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(ok)

