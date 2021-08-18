import random
import collections
import sys
input = sys.stdin.readline
enum = enumerate
inf = 1001001001


def linput(ty=int, cvt=list):
    return cvt(list(map(ty, input().split())))


def vinput(rep=1, ty=int, cvt=list):
    return cvt(ty(input().rstrip()) for _ in "*" * rep)


def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def ran():
    vRan = [random.randint(1, 10),
            random.randint(0, 10),
            random.randint(1, 100)]
    return vRan


def bye(res):
    sT = "No Yes".split()
    print((sT[res]))


def sol_n(a, b, c):
    res = 0
    cnt = 0
    while cnt < c:
        res += 1
        cnt += a
        if res % 7 == 0:
            cnt += b
    return res


def sol(a, b, c):

    res = 0
    L = -(-a // c)
    R = (b // c)
    res = R - L + 1

    return res


def deb():
    vI = ran()
    I = sol_n(*vI)
    J = sol(*vI)
    if 1:
        print((vI, I, J))


def main():
    vI = linput()
    print((sol(*vI)))


def __starting_point():
    main()


__starting_point()
