MOD = 10 ** 9 + 7


def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n, m = INTM()
    b_sts = [False] * n
    for i in range(m):
        b = INT()
        b -= 1
        b_sts[b] = True

    step = [0] * (n + 2)
    step[1] = 1
    for i in range(n):
        if b_sts[i]:
            continue
        else:
            step[i + 2] = (step[i + 1] + step[i]) % MOD
    print(step[-1] % MOD)


def __starting_point():
    do()


__starting_point()
