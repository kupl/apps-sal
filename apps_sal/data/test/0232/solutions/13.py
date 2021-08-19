(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sum(b)
d = [0] * m
for i in range(c):
    d[a[i] - 1] += 1
e = 0
for i in range(n - c + 1):
    if i != 0:
        d[a[i - 1] - 1] -= 1
        d[a[i + c - 1] - 1] += 1
    if d == b:
        e = 1
        break
if e == 0:
    print('NO')
else:
    print('YES')
