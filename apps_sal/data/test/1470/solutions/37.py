import sys


def I():
    return int(sys.stdin.readline().rstrip())


x = I() - 1
print(x // 11 * 2 + 1 + x % 11 // 6)
