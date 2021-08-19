import sys


def pprint(s):
    return print(' '.join(map(lambda x: str(x), s)))


def input():
    return sys.stdin.readline().strip()


ipnut = input
mod = 1000000007
for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    pprint(reversed(p))
