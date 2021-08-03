import sys
sys.setrecursionlimit(1000000)


def rec(n):
    if n == 1:
        return 1
    return rec(n // 2) * 2 + 1


n = int(input())
print(rec(n))
