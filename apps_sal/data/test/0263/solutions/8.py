n, m = int(input()), int(input())
a = []
for i in range(n):
    a.append(int(input()))
ma = max(a) + m
m -= max(a) * n - sum(a)
mi = max(a) + max(0, (m + n - 1) // n)
print(mi, ma)

