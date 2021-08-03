import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = list(map(int, readline().split()))

    def rec(x):
        if x < 4:
            ans = 0
            for i in range(1, x + 1):
                ans ^= i
            return ans

        p = 0
        y = 1
        while y << 1 <= x:
            y <<= 1
            p += 1

        return (1 << p) * ((x - y + 1) % 2) + rec(x & ~(1 << p))

    if A == 0:
        print((rec(B)))
    else:
        print((rec(B) ^ rec(A - 1)))
    return


def __starting_point():
    main()


__starting_point()
