n, k, m = map(int, input().split())
a = list(map(int, input().split()))
g = n * m
for i in a:
    g -= i
print(max(g, 0) if g <= k else -1)
