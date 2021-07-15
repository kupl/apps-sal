n, m = map(int, input().split())
a = [0] * m
for i in range(n):
    b = list(input().rstrip())
    for j in range(m):
        if (b[j] == '*'):
            a[j] = max(a[j], n - i)
ma = 0
mi = 0
for i in range(m - 1):
    ma = max(ma, a[i + 1] - a[i])
    mi = min(mi, a[i + 1] - a[i])
print(ma, -mi)
