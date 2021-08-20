import collections
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        if N == 1:
            print('Second')
            continue
        c = collections.Counter(A)
        f = True
        for k in list(c.keys()):
            if c[k] % 2 == 1:
                f = False
                break
        if f or N % 2 == 1:
            print('Second')
        else:
            print('First')


def __starting_point():
    main()


__starting_point()
