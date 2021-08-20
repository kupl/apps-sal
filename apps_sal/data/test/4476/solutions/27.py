import sys
input = sys.stdin.readline


def getInt():
    return int(input())


def getVars():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


def getStr():
    return input().strip()


t = getInt()
for i in range(t):
    (a, b) = getVars()
    if a == b:
        print(0)
    elif a > b:
        if a % 2 == b % 2:
            print(1)
        else:
            print(2)
    elif a % 2 == b % 2:
        print(2)
    else:
        print(1)
