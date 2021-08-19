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


n = getInt()
for i in range(n):
    s = getStr()
    if s[-2:] == 'po':
        print('FILIPINO')
    if s[-2:] == 'su':
        print('JAPANESE')
    if s[-5:] == 'mnida':
        print('KOREAN')
