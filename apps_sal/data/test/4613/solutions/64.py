from collections import deque, defaultdict
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
    (N, M) = MI()
    V = [[] for _ in range(N)]
    E = []
    for i in range(M):
        (a, b) = MI1()
        V[a].append(b)
        V[b].append(a)
        E.append((a, b))
    ans = 0
    for (a, b) in E:
        used = [0] * N
        flag = True
        q = deque([a])
        used[a] = 1
        while q:
            cur = q.popleft()
            for nv in V[cur]:
                if (a, b) == (cur, nv) or (a, b) == (nv, cur):
                    continue
                if used[nv]:
                    continue
                if nv == b:
                    flag = False
                    q = []
                    break
                q.append(nv)
                used[nv] = 1
        if flag:
            ans += 1
    print(ans)


def __starting_point():
    solve()


__starting_point()
