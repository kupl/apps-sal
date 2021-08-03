import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))

        if n % 2:
            print("Second")
        else:
            D = Counter(A)
            for v in list(D.values()):
                if v % 2:
                    print("First")
                    break
            else:
                print("Second")


def __starting_point():
    resolve()


__starting_point()
