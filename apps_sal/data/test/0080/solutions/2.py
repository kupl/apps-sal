import math


def gcd(x, y):
    while x and y:
        x %= y
        if x:
            y %= x
    return x + y


def lcm(x, y):
    return x * y // gcd(x, y)


tl, tr, tx, ty = input().split()
l = int(tl)
r = int(tr)
x = int(tx)
y = int(ty)
t = []
cnt = 0
for i in range(1, int(math.sqrt(y)) + 1):
    if y % i == 0 and i >= l and i <= r:
        t.append(i)
        cnt += 1
    if y % i == 0 and i * i != y and y // i >= l and y // i <= r:
        t.append(y // i)
        cnt += 1
#for i in t:print(i)
ans = 0
for i in range(cnt):
    for j in range(cnt):
        if gcd(t[i], t[j]) == x and t[i] * t[j] == x * y:
            ans += 1
print(ans)
