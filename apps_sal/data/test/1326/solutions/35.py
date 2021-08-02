import numba
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    @numba.njit
    def solve(n):
        r = 0
        for i1 in range(1, n + 1):
            y = n // i1
            r += y * (y + 1) // 2 * i1
        return r
    no = int(input())
    print(solve(no))


def __starting_point():
    main()


__starting_point()
