import sys
readline = sys.stdin.readline
ans = 0
N = int(readline())
pa = pb = 0
cur = -1
for i in range(N):
    (a, b) = map(int, readline().split())
    ans += max(0, min(a, b) - max(pa, pb) + 1)
    mi = min(a, b) + 1
    (pa, pb) = (max(mi, a), max(mi, b))
print(ans)
