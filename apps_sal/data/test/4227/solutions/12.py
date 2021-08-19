from itertools import permutations
(N, M) = map(int, input().split())
adj = [set() for i in range(N + 1)]
for i in range(M):
    (u, v) = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)


def good(p):
    for i in range(N - 1):
        if p[i + 1] not in adj[p[i]]:
            return False
    return True


ans = 0
for p in permutations(range(2, N + 1)):
    if good([1] + list(p)):
        ans += 1
print(ans)
