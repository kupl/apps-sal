import sys


def read():
    return sys.stdin.readline().rstrip()


def readi():
    return int(sys.stdin.readline())


def writeln(x):
    return sys.stdout.write(str(x) + '\n')


def write(x):
    return sys.stdout.write(x)


(a, b) = map(int, read().split())
year = 0
while a <= b:
    a *= 3
    b *= 2
    year += 1
writeln(year)
