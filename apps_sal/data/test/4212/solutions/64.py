N, M, Q = list(map(int, input().split()))
G = []
for i in range(Q):
    a, b, c, d = list(map(int, input().split()))
    G.append([a, b, c, d])

ans = 0


def dfs(s):
    nonlocal ans
    if len(s) == N:
        now = 0
        for a, b, c, d in G:
            if s[b - 1] - s[a - 1] == c:
                now += d
        ans = max(ans, now)
        return

    for i in range(s[-1], M):
        dfs(s + [i])


s = [0]
dfs(s.copy())

print(ans)
