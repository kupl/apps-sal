(q, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = list(map(int, input().split()))
z = [0] * q
for i in range(1, q):
    z[i] = a[i] - a[i - 1]
z[0] = w - a[q - 1] + a[0]
z = z + z + z
x = [0] * q
for i in range(1, q):
    x[i] = s[i] - s[i - 1]
x[0] = w - s[q - 1] + s[0]
b = False
for i in range(0, q + 1):
    if z[i:i + q] == x:
        b = True
if b:
    print('YES')
else:
    print('NO')
