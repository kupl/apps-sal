(n, m) = map(int, input().split())
a = list(map(int, input().split()))
rec = []
pre = 0
for i in range(n):
    rec.append((a[i] + pre) // m)
    pre = (a[i] + pre) % m
print(' '.join(map(str, rec)))
