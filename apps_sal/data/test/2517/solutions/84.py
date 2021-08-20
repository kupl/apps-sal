import heapq
import sys
import itertools
sys.setrecursionlimit(10 ** 7)


def bfs(cost, node):
    root[node] = min(root[node], cost)
    for (next_c, next_n) in way[node]:
        if root[next_n] == 10 ** 9:
            heapq.heappush(q, [cost + next_c, next_n])
    return


(N, M, R) = list(map(int, input().split()))
r = list(map(int, input().split()))
way = [[] for i in range(N)]
for _ in range(M):
    (A, B, C) = list(map(int, input().split()))
    way[A - 1].append([C, B - 1])
    way[B - 1].append([C, A - 1])
made = []
for start in r:
    root = [10 ** 9] * N
    q = [[0, start - 1]]
    heapq.heapify(q)
    while q:
        temp = heapq.heappop(q)
        if root[temp[1]] == 10 ** 9:
            bfs(temp[0], temp[1])
    made.append(root)
ans = 10 ** 9
for order in itertools.permutations([i for i in range(len(r))]):
    temp = 0
    for i in range(len(order) - 1):
        fro = r[order[i]]
        aft = r[order[i + 1]]
        temp += abs(made[order[i]][aft - 1] - made[order[i]][fro - 1])
    ans = min(ans, temp)
print(ans)
