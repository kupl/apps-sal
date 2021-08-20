import heapq
(H, W) = map(int, input().split())
C = []
for i in range(10):
    C.append(list(map(int, input().split())))
INF = float('inf')


def dfs(x):
    memo = [INF] * 10
    memo[x] = 0
    hq = [(0, x)]
    heapq.heapify(hq)
    while hq:
        (cost, step) = heapq.heappop(hq)
        if cost > memo[step]:
            continue
        for (j, c) in enumerate(C[step]):
            if memo[j] > memo[step] + c:
                memo[j] = memo[step] + c
                heapq.heappush(hq, (memo[j], j))
    return memo[1]


A = [0] * 10
for h in range(H):
    for w in map(int, input().split()):
        if w == -1:
            continue
        else:
            A[w] += 1
ans = 0
for (number, a) in enumerate(A):
    ans += a * dfs(number)
print(ans)
