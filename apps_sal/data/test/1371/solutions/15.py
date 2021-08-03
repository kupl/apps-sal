import sys


def solve():
    input = sys.stdin.readline
    S = int(input())
    mod = 7 + 10 ** 9
    DP = [0] * (S + 1)
    DP[0] = 1
    for i in range(S):
        if DP[i] == 0:
            continue
        for j in range(3, S + 1):
            if i + j > S:
                break
            DP[i + j] += DP[i]
            DP[i + j] %= mod
    print(DP[S])

    return 0


def __starting_point():
    solve()


__starting_point()
