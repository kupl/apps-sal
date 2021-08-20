(n, m) = map(int, input().split())
h = list(map(int, input().split()))
c = 0
d = [0] * n
for i in range(m):
    (a, b) = map(int, input().split())
    d[a - 1] = max(d[a - 1], h[b - 1])
    d[b - 1] = max(d[b - 1], h[a - 1])
for i in range(n):
    if h[i] > d[i]:
        c += 1
print(c)
