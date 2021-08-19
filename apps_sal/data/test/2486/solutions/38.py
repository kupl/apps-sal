import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():

    def need(m):
        s = 1
        for i in range(n):
            if i == m:
                continue
            s |= s << aa[i]
            s &= mask
        if s >> k - aa[m]:
            return True
        return False
    (n, k) = MI()
    mask = (1 << k) - 1
    aa = LI()
    aa.sort()
    for i in range(n):
        if aa[i] > k:
            aa = aa[:i]
            break
    n = len(aa)
    l = -1
    r = n
    while l + 1 < r:
        m = (l + r) // 2
        if need(m):
            r = m
        else:
            l = m
    print(l + 1)


main()
