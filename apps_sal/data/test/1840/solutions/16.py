s, b = map(int, input().split())
a = list(map(int, input().split()))
d = []
for i in range(b):
    x, y = map(int, input().split())
    d.append((x, y, i + 1))

d.sort()
f = [d[0][1]]
for i in range(1, b):
    f.append(f[-1] + d[i][1])


for i in range(s):
    if d[0][0] > a[i]:
        print(0, end=' ')
    elif d[-1][0] <= a[i]:
        print(f[-1])
    else:
        L = 0
        R = b - 1
        while R - L > 1:
            m = (L + R) // 2
            if d[m][0] <= a[i]:
                L = m
            else:
                R = m
        print(f[L], end=' ')

