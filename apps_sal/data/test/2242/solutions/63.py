import sys
import collections


def resolve(in_):
    s = next(in_).strip()
    mod = 2019
    dp = [0] * (len(s) + 1)
    ch0 = ord(b'0')
    for i, b in enumerate(reversed(s), 1):
        dp[i] = (dp[i - 1] + (b - ch0) * pow(10, i, mod)) % mod

    return sum(v * (v - 1) // 2 for v in list(collections.Counter(dp).values()))


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


def __starting_point():
    main()


__starting_point()
