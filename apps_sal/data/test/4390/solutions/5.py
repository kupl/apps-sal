import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)
