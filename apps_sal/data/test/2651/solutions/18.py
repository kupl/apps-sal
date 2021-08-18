import sys


def main():
    p = 10**9 + 7

    def totsum(l, n):
        s = 0
        t = 0
        for i in range(n // 2):
            t = t + l[-1 - i] - l[i]
            s = (s + t) % p
        s = (2 * s - (1 - n & 1) * t) % p
        return s
    n, m = list(map(int, input().split()))
    x = list(map(int, sys.stdin.readline().strip().split()))
    y = list(map(int, sys.stdin.readline().strip().split()))

    print(((totsum(x, n) * totsum(y, m)) % p))


def __starting_point():
    main()


__starting_point()
