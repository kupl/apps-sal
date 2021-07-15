import sys
import numpy as np

stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    cumA = np.cumsum(A)
    total = cumA[-1]
    ans = 10 ** 10000
    for a in cumA[:-1]:
        ans = min(ans, abs(a - (total - a)))
    print(ans)


def __starting_point():
    main()

__starting_point()
