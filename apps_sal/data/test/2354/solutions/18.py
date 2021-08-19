import sys


def query(n, x, y):
    num = (x - 1) * n // 2 + (y + 1) // 2
    factor = (x + 1) % 2 if n % 2 == 1 else 0
    return num + factor if (x + y) % 2 == 0 else (n * n + 1) // 2 + num


(n, q) = map(int, sys.stdin.readline().split())
for line in sys.stdin:
    print(query(n, *map(int, line.split())))
