import sys
import os


def solve(s, k):
    occ = [0] * 26
    for i in range(len(s)):
        occ[ord(s[i]) - ord('A')] += 1

    result = None
    for i in range(k):
        if result is None:
            result = occ[i]
        else:
            result = min(result, occ[i])

    return result * k


def main():
    n, k = map(int, input().split())
    s = input()
    print(solve(s, k))


def __starting_point():
    main()


__starting_point()
