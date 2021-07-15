import itertools
import sys
from typing import List

sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = lmi()
        solve(N, A)

def rfe(S):
    for k, v in itertools.groupby(S):
        yield k, len(list(v))


def solve(N: int, A: List[int]) -> str:
    A.sort()
    if len(A) % 2 == 0:
        if all(count % 2 == 0 for k, count in rfe(A)):
            print('Second')
        else:
            print('First')
    else:
        print('Second')


def __starting_point():
    main()


__starting_point()
