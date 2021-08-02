import sys
input = sys.stdin.readline


def gcd(a, b):
    if a > b:
        a, b = b, a
    while True:
        a, b = b % a, a
        if a == 0:
            return b


def solve(l, r, a, b, lcm):
    mx = max(a, b)
    d1 = l // lcm
    d2 = r // lcm
    lr = l % lcm
    rr = r % lcm
    c = 0
    if lr > mx:
        c += (lcm - lr)
    else:
        c += (lcm - mx)
    if rr >= mx:
        c += (rr - mx + 1)
    c += (d2 - d1 - 1) * (lcm - mx)
    return c


for i in ' ' * int(input()):
    a, b, q = map(int, input().split())
    g = gcd(a, b)
    lcm = a * b // g
    mx = max(a, b)
    for j in ' ' * q:
        l, r = map(int, input().split())
        print(solve(l, r, a, b, lcm), end=' ')
    print()
