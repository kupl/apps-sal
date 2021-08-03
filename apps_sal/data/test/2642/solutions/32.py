from math import gcd
n = int(input())
p = 10**9 + 7
iwashi = {}
bad = 0
ans = 1
for i in range(n):
    x, y = list(map(int, input().split()))
    if(x == 0 and y == 0):
        bad += 1
        continue
    elif(x == 0):
        try:
            iwashi[(0, 1)] += 1
        except KeyError:
            iwashi[(0, 1)] = 1
            continue
    elif(y == 0):
        try:
            iwashi[(1, 0)] += 1
        except KeyError:
            iwashi[(1, 0)] = 1
        continue
    else:
        g = gcd(x, y)
        x, y = x // g, y // g
        if x < 0:
            x, y = -x, -y
        try:
            iwashi[(x, y)] += 1
        except KeyError:
            iwashi[(x, y)] = 1

for x, y in iwashi:
    a = iwashi[(x, y)]
    if y > 0:
        rx, ry = y, -x
    else:
        rx, ry = -y, x
    try:
        b = iwashi[(rx, ry)]
        iwashi[(rx, ry)] = 0
    except KeyError:
        b = 0
    ans *= pow(2, a, p) + pow(2, b, p) - 1
    ans %= p
    iwashi[(x, y)] = 0
print(((ans + bad - 1) % p))
