from sys import stdin


def input():
    return stdin.readline().rstrip()


for _ in range(int(input())):
    L = int(input())
    lockSort = []
    s = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for (i, c) in enumerate(s):
        if l[i] == 0:
            lockSort.append(c)
    lockSort = sorted(lockSort)[::-1]
    cnt = 0
    for (i, c) in enumerate(s):
        if l[i] == 1:
            print(c, end=' ')
        else:
            print(lockSort[cnt], end=' ')
            cnt += 1
    print()
