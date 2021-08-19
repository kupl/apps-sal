from fractions import Fraction
n = int(input())
l1 = []
d2 = {}
for i in range(0, n):
    (x, y) = map(int, input().split())
    for item in l1:
        if x == item[0]:
            if 'inf' not in d2:
                d2['inf'] = [x]
            elif x not in d2['inf']:
                d2['inf'].append(x)
        else:
            slope = Fraction(y - item[1], x - item[0])
            c = Fraction(y, 1) - slope * Fraction(x, 1)
            if slope not in d2:
                d2[slope] = [c]
            elif c not in d2[slope]:
                d2[slope].append(c)
    l1.append((x, y))
z = 0
ans = 0
f = 0
for k in d2:
    z += len(d2[k])
for k in d2:
    x = len(d2[k])
    f = f + x
    ans += x * (z - f)
print(ans)
