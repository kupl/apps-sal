import collections
import copy


def dfs(i, basho, memo):
    nonlocal ans
    # print(i,basho,memo)
    if memo[basho] == 1:
        return
    memo[basho] = 1
    if i == n:
        if sum(memo) == n:
            ans += 1
        return
    tmp = collections.Counter(graph[basho])
    # print(tmp)
    for next_basho in tmp.keys():
        copy_memo = copy.copy(memo)
        dfs(i + 1, next_basho, copy_memo)


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

memo = [0 for i in range(n + 1)]
ans = 0
dfs(1, 1, memo)
print(ans)
