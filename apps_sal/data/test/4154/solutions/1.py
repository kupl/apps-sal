n, m = list(map(int, input().split()))
l, r = 1, n

for i in range(m):
    a, b = list(map(int, input().split()))
    l = max(l, a)
    r = min(r, b)

print((max(r - l + 1, 0)))

