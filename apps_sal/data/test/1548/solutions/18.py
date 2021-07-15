import sys

input = sys.stdin.readline


def read_i():
    return list(map(int, input().split()))


def read_is(n=1):
    return [read_i() for _ in range(n)]


n = int(input())
ls = read_i()
ls.sort()
print(sum(ls[:n // 2])**2 + sum(ls[n // 2:])**2)
