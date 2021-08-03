from collections import deque
N, M = list(map(int, input().split()))

ls = [deque([]) for _ in range(N)]

for i in range(M):
    a, b, c = list(map(int, input().split()))
    a, b = a - 1, b - 1
    ls[a].append([b, c])
cost = [-(10**10) * N] * N
cost[0] = 0

for i in range(N):
    update = False
    q = [deque(m for m in l) for l in ls]
    for j in range(N):
        if cost[j] != -(10**10) * N:
            while q[j]:
                b, c = q[j].pop()
                if cost[b] < cost[j] + c:
                    cost[b] = cost[j] + c
                    update = True
    if i == 0:
        Max = cost[N - 1]
    elif i < N - 1:
        Max = max(Max, cost[N - 1])

if update == True and Max < cost[N - 1]:
    print('inf')
else:
    print(Max)
