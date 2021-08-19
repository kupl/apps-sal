import sys
from collections import Counter


def main(args):
    n = int(input())
    counter = Counter()
    for _ in range(n - 1):
        (u, v) = list(map(int, input().split()))
        counter[u] += 1
        counter[v] += 1
    s = 0
    for c in range(n + 1):
        s += counter[c] == 1
    print(s)


def __starting_point():
    return main(sys.argv)


__starting_point()
