import math as m
n = int(input())
a = [int(z) for z in input().split()]
ans = 0


def sq(a):
    tmp = int(m.sqrt(a))
    s = tmp * tmp
    tmp += 1
    b = tmp * tmp
    if abs(a - s) < abs(a - b):
        return abs(a - s)
    else:
        return abs(a - b)


d = []
for i in range(n):
    d.append((sq(a[i]), a[i]))
d.sort()
for i in range(n // 2):
    ans += d[i][0]
for i in range(n // 2, n):
    if d[i][0] == 0:
        if d[i][1] == 0:
            ans += 2
        else:
            ans += 1
print(ans)
