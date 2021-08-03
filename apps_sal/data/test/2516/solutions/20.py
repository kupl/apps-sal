import collections
import sys
sys.setrecursionlimit(10 ** 8)


def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]


def main():
    N, P = ZZ()
    S = input()
    output = 0

    if P in {2, 5}:
        for i in range(N):
            if int(S[i]) % P == 0:
                output += i + 1
        print(output)
        return

    dp = [0] * (N + 1)
    ex = 1
    for i in range(N):
        dp[i + 1] = (int(S[-1 - i]) * ex + dp[i]) % P
        ex *= 10
        ex %= P

    d = collections.defaultdict(int)
    for i in range(N + 1):
        d[dp[i]] += 1

    for i in list(d.keys()):
        output += (d[i] * (d[i] - 1) // 2)
    print(output)

    return


def __starting_point():
    main()


__starting_point()
