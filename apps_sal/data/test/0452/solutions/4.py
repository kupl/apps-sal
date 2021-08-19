(p, q) = tuple(map(int, input().split()))
n1 = input().split()
n = int(n1[0])
a = list(map(int, input().split()))
x = 1
y = a[n - 1]
for i in range(n - 2, -1, -1):
    x1 = a[i] * y + x
    x = y
    y = x1
if p * x == q * y:
    print('YES')
else:
    print('NO')
