import sys
from collections import defaultdict
from itertools import product

input = sys.stdin.readline

P = 10 ** 9 + 7


def is_ok(a, b, c, d):
    s = "".join((a, b, c, d))
    if ("AGC" in s) or ("ACG" in s) or ("GAC" in s):
        return False
    if (s[0] == "A" and s[2:4] == "GC") or (s[0:2] == "AG" and s[3] == "C"):
        return False
    return True


def main():
    N = int(input())

    dp = [defaultdict(int) for _ in range(N + 1)]
    dp[0][("T", "T", "T")] = 1

    for i in range(N):
        for a, b, c, d in product("ACGT", repeat=4):
            if is_ok(a, b, c, d):
                dp[i + 1][(b, c, d)] = (dp[i + 1][(b, c, d)] + dp[i][(a, b, c)]) % P

    ans = 0
    for v in list(dp[N].values()):
        ans = (ans + v) % P
    print(ans)


def __starting_point():
    main()


__starting_point()
