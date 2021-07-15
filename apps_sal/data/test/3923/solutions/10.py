n, a, b = map(int, input().split())
x, y = 0, 0
ok = False
for i in range(n // a + 1):
    if (n - a * i) % b == 0:
        ok = True
        x, y = i, (n - a * i) // b
        break
if not ok:
    print(-1)
    return
pos = 1
for i in range(x):
    print(pos + a - 1, end=' ')
    for j in range(a - 1):
        print(pos + j, end=' ')
    pos += a

for i in range(y):
    print(pos + b - 1, end=' ')
    for j in range(b - 1):
        print(pos + j, end=' ')
    pos += b

