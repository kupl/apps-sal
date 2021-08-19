a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
t = n
t -= a1 * (k1 - 1)
t -= a2 * (k2 - 1)
if t <= 0:
    print(0, end=' ')
else:
    print(t, end=' ')
t = n
ans = 0
if k1 < k2:
    while t >= k1 and a1 > 0:
        t -= k1
        a1 -= 1
        ans += 1
    while t >= k2 and a2 > 0:
        t -= k2
        a2 -= 1
        ans += 1
else:
    while t >= k2 and a2 > 0:
        t -= k2
        a2 -= 1
        ans += 1
    while t >= k1 and a1 > 0:
        t -= k1
        a1 -= 1
        ans += 1
print(ans)
