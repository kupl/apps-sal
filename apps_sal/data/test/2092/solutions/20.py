from sys import stdin

input = stdin.readline


def works(mid):
    ag = A[-mid]
    MAX = 0
    cur = 0
    out = N + 1
    for l, r, d in traps:
        if d <= ag:
            continue
        if r > MAX:
            out += (r - max(l - 1, MAX)) * 2
            MAX = r
    return out <= time


S, N, T, time = map(int, input().split())
A = list(map(int, input().split()))
traps = [tuple(map(int, input().split())) for _ in range(T)]
traps.sort()
A.sort()


lo = 0
hi = S + 1
while hi - lo > 1:
    mid = (hi + lo) // 2
    if works(mid):
        lo = mid
    else:
        hi = mid

print(lo)
