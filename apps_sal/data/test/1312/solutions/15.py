import sys


def solve():
    (n, m) = map(int, input().split())
    res = [0] * m
    for i in range(n):
        res[i % m] += 1
    return ' '.join(map(str, res))


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
