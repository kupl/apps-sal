import bisect
n = int(input())
colors = [-1]*(n+1)
for _ in range(n):
    a = int(input())
    idx = bisect.bisect_left(colors, a)-1
    colors[idx] = a
print((colors[::-1].index(-1)))

