import sys
sys.setrecursionlimit(10 ** 6)

def solve():
    N, Q = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = [int(x) - 1 for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    ans = [0] * N
    for i in range(Q):
        p, x = list(map(int, input().split()))
        p -= 1
        ans[p] += x
    def dfs(cur, pre):
        for to in graph[cur]:
            if to == pre:
                continue
            ans[to] += ans[cur]
            dfs(to, cur)
    dfs(0, -1)
    print((*ans))
    return

solve()

