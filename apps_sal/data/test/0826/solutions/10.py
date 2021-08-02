
import sys
# sys.setrecursionlimit(500000)


input = sys.stdin.readline

N = int(input().strip())
k_max = None

# k_maxを求める
ok = 0
ng = 2 * (N + 1)
while abs(ok - ng) > 1:  # 条件を満たすindex ok と 条件を満たさないindex ng が ちょうど 1 ズレる(ちょうどokとngで境界になる)まで続ける
    mid = (ok + ng) // 2
    if mid * (mid + 1) <= 2 * (N + 1):
        ok = mid
    else:
        ng = mid
k_max = ok
# eprint(k_max)
print(N - k_max + 1)
