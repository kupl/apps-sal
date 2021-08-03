import sys
input = sys.stdin.readline


def value(x, y):
    ANS = (x + y - 2) * (x + y - 1) // 2
    return ANS + x


t = int(input())
for tests in range(t):
    x1, y1, x2, y2 = list(map(int, input().split()))

    print(1 + (x2 - x1) * (y2 - y1))
