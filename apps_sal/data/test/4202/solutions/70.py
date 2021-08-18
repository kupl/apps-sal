
def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    l, r = INTM()
    mods = []
    for i in range(l, min(l + 3000, r + 1)):
        mods.append(i % 2019)

    ans = 2018
    ml = len(mods)
    for i in range(ml - 1):
        for j in range(i + 1, ml):
            ans = min(ans, (mods[i] * mods[j]) % 2019)

    print(ans)


def __starting_point():
    do()


__starting_point()
