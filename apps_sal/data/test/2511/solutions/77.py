# E - Virus Tree 2
# https://atcoder.jp/contests/abc133/tasks/abc133_e

from heapq import heapify, heappop, heappush


def permutation(n, k, MOD):
    s = 1
    for _ in range(k):
        s *= n
        s %= MOD
        n -= 1
    return s


def dfs(c):
    nonlocal ans
    q = [c]
    heapify(q)
    while q:
        cur = heappop(q)
        if cur == 0:
            exclusion = 1
        else:
            exclusion = 2
        visited[cur] = True
        next_cnt = 0
        for i in edges[cur]:
            if not visited[i]:
                heappush(q, i)
                next_cnt += 1
        if k - exclusion - next_cnt < 0:
            print(0)
            return
        ans *= permutation(k - exclusion, next_cnt, MOD)
        ans %= MOD


n, k = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n - 1)]
AB = [(a - 1, b - 1) for a, b in AB]

MOD = 10 ** 9 + 7

edges = [[] for _ in range(n)]
for itr, (a, b) in enumerate(AB):
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * n

ans = k
dfs(0)

print(ans)
