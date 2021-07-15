n, m = list(map(int, input().split()))
t = set()
for i in range(m):
    x, y = list(map(int, input().split()))
    t.add(x)
    t.add(y)
for i in range(1, n + 1):
    m = i if i not in t else m
print(n - 1)
for i in range(1, n + 1):
    if i != m:
        print(i, m)

