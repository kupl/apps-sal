import sys


def inp():
    return sys.stdin.readline()


def mi():
    return map(int, inp().split())


def li():
    return list(map(int, inp().split()))


def mf():
    return map(float, inp().split())


def lf():
    return list(map(float, inp().split()))


A = int(inp())
B = int(inp())
C = int(inp())
D = int(inp())
E = int(inp())
K = int(inp())
print('Yay!' if E - A <= K else ':(')
