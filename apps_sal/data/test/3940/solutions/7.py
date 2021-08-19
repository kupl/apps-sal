(n, m) = map(int, input().split())
d = n
for i in range(m):
    (l, r) = map(int, input().split())
    d = min(d, r - l + 1)
print(d)
for i in range(n):
    print(i % d, end=' ')
