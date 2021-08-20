(n, m) = list(map(int, input().split(' ')))
b = []
a = set()
for _ in range(m):
    (i, j) = list(map(int, input().split(' ')))
    a.add(i)
    a.add(j)
a = list(a)
i = 0
for i in range(1, n + 1):
    if i not in a:
        break
print(n - 1)
for j in range(1, n + 1):
    if i != j:
        print(i, j)
