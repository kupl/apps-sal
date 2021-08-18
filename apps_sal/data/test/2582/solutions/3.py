from collections import deque
from sys import stdin


def inv(perm):
    invp = [None] * len(perm)
    for i, p in enumerate(perm):
        invp[p] = i
    return invp


def main():
    n = int(stdin.readline())
    p = [int(x) - 1 for x in stdin.readline().split()]
    invp = inv(p)

    nexL = [None] * n
    nexR = [None] * n
    q = deque()
    for i in range(0, n):
        while q and p[q[-1]] <= p[i]:
            q.pop()
        nexL[i] = -1 if not q else q[-1]
        q.append(i)
    q.clear()
    for i in range(n - 1, -1, -1):
        while q and p[q[-1]] <= p[i]:
            q.pop()
        nexR[i] = n if not q else q[-1]
        q.append(i)

    res = 0
    for i in range(0, n):
        if i - nexL[i] < nexR[i] - i:
            for j in range(nexL[i] + 1, i):
                x = p[i] - p[j] - 1
                res += int(x >= 0 and i < invp[x] <= nexR[i])
        else:
            for j in range(i + 1, nexR[i]):
                x = p[i] - p[j] - 1
                res += int(x >= 0 and nexL[i] <= invp[x] < i)
    print(res)


main()
