from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)


def int1(x):
    return int(x) - 1


def II():
    return int(input())


def MI():
    return list(map(int, input().split()))


def MI1():
    return list(map(int1, input().split()))


def LI():
    return list(map(int, input().split()))


def LI1():
    return list(map(int1, input().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def MS():
    return input().split()


def LS():
    return list(input())


def LLS(rows_number):
    return [LS() for _ in range(rows_number)]


def printlist(lst, k=' '):
    print(k.join(list(map(str, lst))))


INF = float('inf')


def solve():
    N = II()
    S = LS()
    q = deque([])
    cnt = 0
    for s in S:
        if s == '(':
            cnt += 1
            q.append(s)
        elif cnt >= 1:
            q.append(s)
            cnt -= 1
        else:
            q.appendleft('(')
            q.append(s)
    for _ in range(cnt):
        q.append(')')
    printlist(q, '')


def __starting_point():
    solve()


__starting_point()
