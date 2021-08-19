import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s) // 2
    p = s.count('p')
    print(n - p)


def __starting_point():
    resolve()


__starting_point()
