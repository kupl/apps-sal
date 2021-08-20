import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
(n, m) = map(int, input().split())
antena = [list(map(int, input().split())) for i in range(n)]
DP = [float('inf')] * (m + 1)
DP[0] = 0
for i in range(1, m + 1):
    DP[i] = i
    for (x, s) in antena:
        l = max(1, x - s)
        r = min(m, x + s)
        if l <= i <= r:
            DP[i] = DP[i - 1]
            break
        elif r < i:
            cost = i - r
            DP[i] = min(DP[i], DP[max(0, l - cost - 1)] + cost)
print(DP[-1])
