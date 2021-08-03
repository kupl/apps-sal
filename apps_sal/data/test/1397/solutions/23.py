n, m = list(map(int, input().split()))
a = set(range(1, n + 1))
for i in range(m):
    a = a - set(map(int, input().split()))
a = list(a)[0]
print(n - 1)
for i in range(1, n + 1):
    if i != a:
        print(a, i)
