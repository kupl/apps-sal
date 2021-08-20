x0 = []
x1 = []
y0 = []
y1 = []
n = int(input())
s = 0
for i in range(n):
    l = list(map(int, input().split()))
    x0.extend([l[0]])
    x1.extend([l[2]])
    y0.extend([l[1]])
    y1.extend([l[3]])
    s += (l[3] - l[1]) * (l[2] - l[0])
lx = max(x1) - min(x0)
ly = max(y1) - min(y0)
if lx == ly and lx * ly == s:
    print('YES')
else:
    print('NO')
