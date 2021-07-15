import collections


n = int(input())
a = [0, 0] + list(map(int, input().split()))

# contruct tree
G = collections.defaultdict(list)
for i in range(2, len(a)):
    G[a[i]].append(i)

# dp[i] represents the number of color needed to make node i be happy
# recursion will get stackover flow, use bottom to top
nodes = []
q = collections.deque([1])
while q:
    node = q.popleft()
    nodes.append(node)
    for v in G[node]:
        q.append(v)

nodes.reverse()

dp = {}
for u in nodes:
    count = 0
    if len(G[u]) == 0: count += 1
    for v in G[u]:
        count += dp[v]
    dp[u] = count


res = sorted(dp.values())
print(' '.join(map(str, res)))

