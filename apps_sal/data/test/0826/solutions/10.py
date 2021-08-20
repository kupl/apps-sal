import sys
input = sys.stdin.readline
N = int(input().strip())
k_max = None
ok = 0
ng = 2 * (N + 1)
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if mid * (mid + 1) <= 2 * (N + 1):
        ok = mid
    else:
        ng = mid
k_max = ok
print(N - k_max + 1)
