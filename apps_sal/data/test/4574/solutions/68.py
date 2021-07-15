import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    ans = 0
    counter = Counter(A)
    vec1 = [k for k, v in list(counter.items()) if v >= 2]
    vec2 = [k for k, v in list(counter.items()) if v >= 4]

    vec1.sort()
    if len(vec1) >= 2:
        ans = vec1[-2] * vec1[-1]

    vec2.sort()
    if len(vec2) >= 1:
        ans = max(ans, vec2[-1] ** 2)

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
