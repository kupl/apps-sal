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


def SMI():
    return input().split()


def SLI():
    return list(input())


def printlist(lst, k=' '):
    print(k.join(list(map(str, lst))))


INF = float('inf')


def solve():
    K = II()
    q = deque([(1, 1)])
    used = [0 for _ in range(K)]
    while len(q) > 0:
        (v, cost) = q.popleft()
        if v == 0:
            print(cost)
            return
        if used[v]:
            continue
        used[v] = 1
        q.appendleft((v * 10 % K, cost))
        q.append(((v + 1) % K, cost + 1))


def __starting_point():
    solve()


__starting_point()
