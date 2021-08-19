import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
plus = []
minus = []
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    plus.append(x + y)
    minus.append(x - y)
print(max(max(plus) - min(plus), max(minus) - min(minus)))
