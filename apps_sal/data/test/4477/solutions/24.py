import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    num = read()
    tot = (num % 10 - 1) * 10
    for i in range(len(str(num))):
        tot += i + 1
    print(tot)
