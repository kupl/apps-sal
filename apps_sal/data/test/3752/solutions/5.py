from sys import stdin, stdout
from random import randrange


k, d, t = map(int, stdin.readline().split())
EPS = 10 ** (-9)
chicken = 100

d = ((k + d - 1) // d) * d

if False:
    stdout.write(str(chicken * t / 100))
else:

    l, r = -1, 2 * t + 10
    while r - l > 1:
        m = (l + r) >> 1

        cnt = m * k + m * (d - k) / 2

        if cnt * 100 / t >= 100:
            r = m
        else:
            l = m

    cnt = l * k + l * (d - k) / 2
    chicken = chicken - cnt * 100 / t
    ans = l * k + l * (d - k)

    if k * 100 / t >= chicken:
        ans += chicken * t / 100
        chicken = 0
    else:
        ans += k
        chicken -= k * 100 / t
        ans += chicken * 2 * t / 100
        chicken = 0

stdout.write(str(ans))
