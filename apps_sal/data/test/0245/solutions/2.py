n = int(input())
x1 = []
x2 = []
y1 = []
y2 = []
S = 0
for i in range(n):
    (a, b, c, d) = list(map(int, input().split()))
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
    S += (c - a) * (d - b)
if (max(x2) - min(x1)) * (max(y2) - min(y1)) == S and max(x2) - min(x1) == max(y2) - min(y1):
    print('YES')
else:
    print('NO')
