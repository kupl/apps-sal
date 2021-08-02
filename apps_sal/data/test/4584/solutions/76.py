n = int(input())

a = [0 for _ in range(n - 1)]
a = [int(s) for s in input().split()]

d = {}

for i in range(n - 1):
    boss = a[i]
    d[boss] = d.setdefault(boss, 0) + 1

for i in range(n):
    ans = d.setdefault(i + 1, 0)
    print(ans)
