import bisect
n = int(input())
colors = [-1]*(n+1)
for _ in range(n):
    a = int(input())
    idx = bisect.bisect_left(colors, a)-1
    colors[idx] = a
print((n-bisect.bisect_left(colors, 0)+1))

