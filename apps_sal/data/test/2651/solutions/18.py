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

    # for j in range(2,m):
    #     ns=(s*(y[j]-y[j-1])) % p
    #     tot2=(tot2 + j*ns) % p
    #     tot1=(tot2+tot1) % p
    # print(tot1)


def __starting_point():
    main()


__starting_point()
