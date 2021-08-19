(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = [[abs(0 - a[0]), 0]]
li = b[0][0]
off = 0
for i in range(n - 1):
    if i % 2 == 0:
        b.append([li, off + abs(a[i] - a[i + 1])])
        off += abs(a[i] - a[i + 1])
    else:
        b.append([li + abs(a[i] - a[i + 1]), off])
        li += abs(a[i] - a[i + 1])
if n % 2 == 0:
    b.append([li + abs(m - a[-1]), off])
else:
    b.append([li, off + abs(m - a[-1])])
ma = b[-1][0]
for i in range(1, len(b)):
    ma = max(ma, b[i][1] - b[i - 1][1] - 1 + b[i][0] + b[-1][1] - b[i][1])
print(ma)
