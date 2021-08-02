import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = []
    for _ in range(n):
        t = deque(list(([int(x) - 1 for x in input().split()])))
        A.append(t)

    que = deque(list(range(n)))
    res = 0
    emp = [False] * n
    while que:
        next_que = deque([])
        check = set()
        while que:
            i = que.popleft()
            if A[i]:
                idx = A[i][0]
                if i not in check and idx not in check and A[idx][0] == i:
                    A[i].popleft()
                    A[idx].popleft()
                    next_que.append(i)
                    next_que.append(idx)
                    check.add(i)
                    check.add(idx)
            else:
                emp[i] = True
        que = next_que
        if que:
            res += 1
    else:
        print((res if all(emp) else -1))


def __starting_point():
    resolve()


__starting_point()
