from fractions import gcd
a, b, c, d = list(map(int, input().split()))
ax, bx, cx, dx = a, b, c, d

a, b, c, d = a * d, b * d, c * b, d * b

monitor = a * b
film = c * d
negru = monitor - film

monitor, negru = monitor // gcd(monitor, negru), negru // gcd(monitor, negru)
ans1 = (negru, monitor)


a, b, c, d = bx, ax, dx, cx
a, b, c, d = a * d, b * d, c * b, d * b

monitor = a * b
film = c * d
negru = monitor - film

monitor, negru = monitor // gcd(monitor, negru), negru // gcd(monitor, negru)
ans2 = (negru, monitor)


if ans1[1] == 0 or ans1[0] / ans1[1] < 0:
    sol = ans2
elif ans2[1] == 0 or ans2[0] / ans2[1] < 0:
    sol = ans1
else:
    if ans1[0] / ans1[1] < ans2[0] / ans2[1]:
        sol = ans1
    else:
        sol = ans2

print('%i/%i' % sol)
