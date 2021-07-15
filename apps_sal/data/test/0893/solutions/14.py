import sys


def readInts(): return [int(x) for x in sys.stdin.readline().split()]


def readInt(): return int(sys.stdin.readline())


def print(x):
    sys.stdout.write(str(x) + '\n')


def solve():
    MOD = int(1e9 + 7)
    d, n = readInts()
    a = [0] + readInts()
    adj: list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = readInts()
        adj[u].append(v)
        adj[v].append(u)

    vis = [False for _ in range(n + 1)]
    f = [0 for _ in range(n + 1)]

    def dfs(cur, root):
        vis[cur] = True

        f[cur] = 1
        for neigh in adj[cur]:
            if vis[neigh]:
                continue
            if not (a[root] <= a[neigh] <= a[root] + d):
                continue
            if a[neigh] == a[root] and neigh < root:
                continue
            dfs(neigh, root)
            f[cur] *= f[neigh] + 1
            f[cur] %= MOD

    ans = 0
    for i in range(1, n + 1):
        vis = [False for _ in range(n + 1)]
        f = [0 for _ in range(n + 1)]
        dfs(i, i)
        ans += f[i]
        ans %= MOD
    print(ans)


def main():
    t = 1
    # t = readInt()
    for _ in range(t):
        solve()


main()

