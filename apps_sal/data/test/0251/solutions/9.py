3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, K, H):
    H.sort(reverse=True)
    while len(H) >= 2 and H[-2] == H[-1]:
        H.pop()

    width = 0
    cnt = 0
    remain = 0
    for i in range(len(H) - 1):
        h = H[i]
        h1 = H[i + 1]

        width += 1

        height = h - h1

        dprint('i={} h={} h1={} width={} height={} cnt={} remain={}'.format(
            i, h, h1, width, height, cnt, remain))

        if height == 0:
            continue

        if remain + width * height < K:
            remain += width * height
            continue

        dh = (K - remain) // width
        dprint('dh={}'.format(dh))
        assert dh <= height
        remain = 0
        height -= dh
        cnt += 1

        if width * height < K:
            remain += width * height
            continue

        dprint('A: height={} cnt={}'.format(height, cnt))

        t = K // width
        assert t >= 1
        dprint('t={}'.format(t))

        sets = height // t - 1
        dprint('sets={}'.format(sets))
        height -= t * sets
        cnt += sets
        dprint('B: height={} cnt={}'.format(height, cnt))

        while width * height >= K:
            height -= t
            cnt += 1
            dprint('C: height={} cnt={}'.format(height, cnt))

        assert width * height < K
        remain += height * width

    assert remain < K
    if remain > 0:
        cnt += 1

    return cnt


def main():
    N, K = [int(e) for e in inp().split()]
    H = [int(e) for e in inp().split()]
    assert len(H) == N
    print(solve(N, K, H))


def __starting_point():
    main()

__starting_point()
