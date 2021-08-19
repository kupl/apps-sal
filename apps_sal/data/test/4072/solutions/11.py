import sys


def read_line():
    return sys.stdin.readline().rstrip('\r\n')


n = int(read_line())
print(n % 2)
