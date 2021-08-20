(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
(x, y) = (b[-1], a[-1])
for i in range(n - 1):
    x ^= a[i]
for j in range(m - 1):
    y ^= b[j]
if x != y:
    print('NO')
else:
    print('YES')
    for i in range(n - 1):
        for j in range(m - 1):
            print(0, end=' ')
        print(a[i])
    for j in range(m - 1):
        print(b[j], end=' ')
    print(x)
