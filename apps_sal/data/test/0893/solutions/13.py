import sys


def readInts():
    return [int(x) for x in sys.stdin.readline().split()]


def readInt():
    return int(sys.stdin.readline())


def solve():
    MOD = int(1000000000.0 + 7)
    (d, n) = readInts()
    a = readInts()
    adj: list = [[] for _ in range(n)]
    for _ in range(n - 1):
        (u, v) = readInts()
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    vis = [False for _ in range(n)]
    f = [0 for _ in range(n)]

    def dfs(cur, root):
        vis[cur] = True
        f[cur] = 1
        for neigh in adj[cur]:
            if vis[neigh]:
                continue
            if not a[root] <= a[neigh] <= a[root] + d:
                continue
            if a[neigh] == a[root] and neigh < root:
                continue
            dfs(neigh, root)
            f[cur] *= f[neigh] + 1
            f[cur] %= MOD
    ans = 0
    for i in range(0, n):
        vis = [False for _ in range(n)]
        f = [0 for _ in range(n)]
        dfs(i, i)
        ans += f[i]
        ans %= MOD
    print(ans)


def main():
    t = 1
    for _ in range(t):
        solve()


main()
