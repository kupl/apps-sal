import sys
import collections
import bisect


def main():
    n = int(input())
    a = [str(i + 1)[0] + str(i + 1)[-1] for i in range(n)]
    b = [str(i + 1)[-1] + str(i + 1)[0] for i in range(n)]
    ac, bc = collections.Counter(a), collections.Counter(b)
    acKeys = list(ac.keys())
    bcKeys = list(bc.keys())
    cnt = 0
    for i in acKeys:
        cnt += ac[i] * bc[i]
    print(cnt)


def __starting_point():
    main()

__starting_point()
