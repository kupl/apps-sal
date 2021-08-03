import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n, x, a, b = list(map(int, I().split()))
    a = abs(a - b)
    print(min(n - 1, a + x))
