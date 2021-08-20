import sys


def input():
    return sys.stdin.readline().strip()


def mapint():
    return map(int, input().split())


sys.setrecursionlimit(10 ** 9)
x = int(input())
cnt = -(-x // 11)
if cnt * 11 - x >= 5:
    print(cnt * 2 - 1)
else:
    print(cnt * 2)
