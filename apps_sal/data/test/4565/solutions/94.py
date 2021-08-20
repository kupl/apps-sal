import sys
import numpy as np
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    S = ns()
    E = np.cumsum([1 if s == 'E' else 0 for s in S][::-1])[::-1]
    W = np.cumsum([1 if s == 'W' else 0 for s in S])
    ans = E + W
    print(np.min(ans) - 1)


def __starting_point():
    main()


__starting_point()
