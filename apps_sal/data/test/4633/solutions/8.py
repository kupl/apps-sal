import sys

input = sys.stdin.readline


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (list(map(int, input().split())))


def digitSum(x):
    c = 0
    while x:
        c += x % 10
        x //= 10
    return c


def solve(x, y):
    if digitSum(x) <= y:
        return 0
    xStr = str(x)
    attempt = 10 ** len(xStr) - x

    for i in range(len(xStr)):
        newNumber = int(xStr[:i + 1]) + 1
        newNumber *= 10 ** (len(xStr) - i - 1)
        if digitSum(newNumber) <= y:
            attempt = newNumber - x
    return attempt


lines = inp()
for i in range(lines):
    v = inlt()
    print(solve(*v))
