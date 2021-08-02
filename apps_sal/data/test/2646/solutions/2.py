from collections import deque
N, M = list(map(int, input().split()))

A = [[] for i in range(N + 1)]

for i in range(M):
    a, b = list(map(int, input().split()))
    A[a].append(b)
    A[b].append(a)


def BFS():
    q = deque()
    q.append(1)
    pre = [0] * (N + 1)
    pre[0] = pre[1] = -1
    while(q):
        x = q.popleft()
        for y in A[x]:
            if pre[y] == 0:
                pre[y] = x
                q.append(y)
    if 0 in pre:
        print('No')
    else:
        print('Yes')
        for i in range(2, N + 1):
            print((pre[i]))


BFS()
