import sys


def input():
    return sys.stdin.readline().strip()


T = int(input())
for i in range(T):
    (a, b, c) = list(map(int, input().split()))
    print((a + b + c) // 2)
