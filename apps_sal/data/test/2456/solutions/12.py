import sys


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    (n, r) = map(int, input().split())
    if n > r:
        print(r * (r + 1) // 2)
    else:
        print(n * (n - 1) // 2 + 1)
