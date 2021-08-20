(n, m) = list(map(int, input().split(' ')))
a = []
for i in range(n):
    x = int(input())
    a.append(x)
a.sort()
mn = 1000000000
for i in range(m - 1, n):
    mn = min(a[i] - a[i - m + 1], mn)
print(mn)
