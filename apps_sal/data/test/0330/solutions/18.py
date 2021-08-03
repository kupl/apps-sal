from math import sqrt
def GI(): return int(input())


def GIS(): return list(map(int, input().split()))
def LGIS(): return list(GIS())


def main():
    p, y = GIS()

    for x in range(y, p, -1):
        for d in range(2, min(p, int(sqrt(x))) + 1):
            if not x % d:
                break
        else:
            return x

    return -1


print(main())
