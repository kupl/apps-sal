import sys


def solve():
    n = int(input())
    avg = sum([list(map(float, input().split()))[1] for _ in range(n)]) / n
    return avg + 5


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
