def main():
    N = int(input())

    # K > 1

    def divisor_set(x):
        ret = set()
        if x > 1:
            ret.add(x)

        d = 2
        while d * d <= x:
            if x % d == 0:
                ret.add(d)
                ret.add(x // d)
            d += 1
        return ret

    # N % K == 1
    # (N-1) % K == 0
    # K > 1

    ans = 0
    ans += len(divisor_set(N - 1))

    # N % K == 0
    # N //= K ---> M
    # (M-1) % K == 0

    for k in divisor_set(N):
        x = N
        while x % k == 0:
            x //= k
        if x % k == 1:
            ans += 1

    print(ans)


def __starting_point():
    main()

# import sys
#
# sys.setrecursionlimit(10 ** 7)
#
# input = sys.stdin.readline
# rstrip()
# int(input())
# map(int, input().split())

__starting_point()
