import sys
3


def sstevk(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


def __starting_point():
    a, b, c = list(map(int, sys.stdin.readline().split()))
    sols = []
    for s in range(0, 9 * 9 + 1):
        x = b * s**a + c
        if x <= 0 or x >= 10**9:
            continue
        if sstevk(x) == s:
            sols.append(x)
    sols.sort()

    print(len(sols))
    print(' '.join(str(x) for x in sols))


__starting_point()
