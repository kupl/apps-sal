from sys import stdin
from sys import setrecursionlimit as SRL; SRL(10**7)
rd = stdin.readline
rrd = lambda: list(map(int, rd().strip().split()))


def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)


n,m,q = rrd()

g = gcd(n,m)
n = n//g
m = m//g

while q:
    sx, sy, ex, ey = rrd()
    sy -= 1
    ey -= 1
    if sx == 1:
        sy = sy//n
    else:
        sy = sy//m

    if ex == 1:
        ey = ey // n
    else:
        ey = ey // m

    if sy == ey:
        print("YES")
    else:
        print("NO")

    q -= 1




