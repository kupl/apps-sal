(n, l) = map(int, input().split())
a = 0
for i in range(1, n + 1):
    a += l + i - 1
m = 10 ** 9
idx = 1
for i in range(1, n + 1):
    if abs(l + i - 1) < m:
        m = abs(l + i - 1)
        idx = i
print(a - (l + idx - 1))
