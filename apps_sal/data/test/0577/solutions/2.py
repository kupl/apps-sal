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
    (n, k) = MI()
    ab = LLI(n)
    pre = 1
    sa = sb = 0
    mask = (1 << k) - 1
    for (a, b) in ab:
        sa += a
        sb += b
        if a + b < k:
            continue
        mn = max(k - b, 0)
        mx = min(a, k - 1)
        now = pre
        for s in range(mn, mx + 1):
            now |= pre << s
        now |= now >> k
        now &= mask
        pre = now
    ans = 0
    for r in range(k):
        if pre >> r & 1:
            ans = max(ans, (sa - r) // k + (sb + r) // k)
    print(ans)


main()
