from collections import deque

int1 = lambda x: int(x) - 1
MOD = 10 ** 9 + 7

N, K = list(map(int, input().split()))
T = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = list(map(int1, input().split()))
    T[a].append(b)
    T[b].append(a)

# dfs
ans = K
for i in range(len(T[0])):
    ans = (ans * (K - i - 1)) % MOD
D = deque(T[0])
visited = {0}

while D:
    v = D.pop()
    visited.add(v)
    for i in range(len(T[v]) - 1):
        ans = (ans * (K - i - 2)) % MOD
    for x in T[v]:
        if x not in visited:
            D.append(x)
print(ans)

