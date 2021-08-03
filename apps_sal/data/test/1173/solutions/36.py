import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [deque(list(map(int, input().split()))) for _ in range(n)]

    que = deque()
    for i in range(n):
        que.append(i)

    res = 0
    while True:
        tmp = deque()
        used = set()
        while que:
            idx = que.popleft()
            if A[idx]:
                a = A[idx][0] - 1
                if idx in used or a in used:
                    continue
                if A[a][0] - 1 == idx:
                    A[idx].popleft()
                    A[a].popleft()
                    used.add(idx)
                    used.add(a)
                    tmp.append(idx)
                    tmp.append(a)
        if tmp:
            res += 1
            que = tmp
        else:
            break

    for a in A:
        if a:
            print((-1))
            break
    else:
        print(res)


def __starting_point():
    resolve()


__starting_point()
