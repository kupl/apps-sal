import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__


def main():
    (n, a, b) = [int(x) for x in input().split()]
    dc = {}
    for i in range(n):
        (x, vx, vy) = [int(x) for x in input().split()]
        nx = x + vx
        ny = a * x + b + vy
        dd = a * nx - ny + b
        if dd not in dc:
            dc[dd] = {}
        if (vx, vy) not in dc[dd]:
            dc[dd][vx, vy] = 0
        dc[dd][vx, vy] += 1
    tot = 0
    for (v, k) in dc.items():
        tt = 0
        pp = 0
        for (_, cc) in k.items():
            tt -= cc * (cc + 1) // 2
            pp += cc
        tt += pp * (pp + 1) // 2
        tot += tt * 2
    print(tot)


def __starting_point():
    main()


__starting_point()
