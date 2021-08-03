n, h, m = map(int, input().split())
a = [h] * n
for _ in range(m):
    l, r, c = map(int, input().split())
    for i in range(l - 1, r):
        a[i] = min(a[i], c)
print(sum(k ** 2 for k in a))
