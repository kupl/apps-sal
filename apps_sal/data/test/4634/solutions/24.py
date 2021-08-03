import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()

for _ in range(t):
    n = read()
    A = readList()
    ri = -1
    for i in range(n - 1, -1, -1):
        if A[i]:
            ri = i
            break
    count = 0
    start = False
    for i in range(n):
        num = A[i]
        if num == 1:
            start = True
        if num == 0 and start and i < ri:
            count += 1

    print(count)
