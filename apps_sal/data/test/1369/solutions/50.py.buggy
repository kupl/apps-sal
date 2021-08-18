from fractions import Fraction
from math import sqrt

n = int(input())
p = []

for i in range(n):
    p.append(list(map(int, input().split())))

ans = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        flag = True
        x1, y1 = p[i][0], p[i][1]
        x2, y2 = p[j][0], p[j][1]
        d = (x2 - x1)**2 + (y2 - y1)**2
        for k in range(n):
            if (i == k or j == k):
                continue
            x3, y3 = p[k][0], p[k][1]
            e = (x3 - x1)**2 + (y3 - y1)**2 + (x3 - x2)**2 + (y3 - y2)**2
            if (d < e):
                flag = False
                break
        if flag:
            ans = sqrt(d) / 2.0

if (ans != 0):
    print(ans)
    return

ans = 100000000

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b = p[i][0], p[i][1]
            c, d = p[j][0], p[j][1]
            e, f = p[k][0], p[k][1]
            if ((a == c == e) or (b == d == f)):
                continue
            ny = (e - a) * (a * a + b * b - c * c - d * d) - (c - a) * (a * a + b * b - e * e - f * f)
            dy = 2 * (e - a) * (b - d) - 2 * (c - a) * (b - f)
            if (dy == 0):
                continue
            py = Fraction(ny, dy)
            if (c != a):
                px = 2 * (b - d) * py - a * a - b * b + c * c + d * d
                px /= 2 * (c - a)
            else:
                px = 2 * (b - f) * py - a * a - b * b + e * e + f * f
                px /= 2 * (e - a)
            r = (c - px)**2 + (d - py)**2
            flag = True
            for l in range(n):
                if (l == i or l == j or l == k):
                    continue
                x, y = p[l][0], p[l][1]
                s = (x - px)**2 + (y - py)**2
                if (r < s):
                    flag = False
                    break
            if (flag):
                q = r.numerator / r.denominator
                q = sqrt(q)
                ans = min(ans, q)

print(ans)
