from sys import stdin


def input():
    return stdin.readline().strip()


a, b, c = list(map(int, input().split()))

print(2 * c + 2 * min(a, b) + (a - min(a, b) > 0 or b - min(a, b) > 0))
