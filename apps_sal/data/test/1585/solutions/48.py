import sys
sys.setrecursionlimit(10 ** 6)


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LC():
    return list(input())


def IC():
    return [int(c) for c in input()]


def MI():
    return map(int, input().split())


(X, Y) = MI()
Out = 1
while X * 2 <= Y:
    Out += 1
    X *= 2
print(Out)
