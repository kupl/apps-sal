import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = [[] for _ in range(N)]
    for i in range(N):
        A[i] = list([int(x) - 1 for x in input().split()])

    # print(A)

    days = 0
    ta = [i for i in range(N)]
    while True:
        ta2 = []
        aset = set()
        for i in ta:
            if len(A[i]) == 0 or i in aset:
                continue
            if i == A[A[i][0]][0]:
                ta2.append(i)
                ta2.append(A[i][0])
                aset |= set([i])
                aset |= set([A[i][0]])
        if len(ta2) > 0:
            for t in ta2:
                A[t].pop(0)
            days += 1
            ta = ta2
        else:
            break

    empty = True
    for i in range(N):
        if len(A[i]) != 0:
            empty = False
            break

    if empty:
        print(days)
    else:
        print((-1))


def __starting_point():
    solve()


__starting_point()
