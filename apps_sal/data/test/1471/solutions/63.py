import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    def dfs(node):
        for adjnode in edges[node]:
            if colors[adjnode[0]] == -1:
                if adjnode[1] % 2 == 0:
                    colors[adjnode[0]] = colors[node]
                else:
                    colors[adjnode[0]] = colors[node] ^ 1
                dfs(adjnode[0])
    n = int(input())
    edges = {e: [] for e in range(n)}
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((v, w))
        edges[v].append((u, w))
    colors = [-1] * n
    colors[0] = 0
    dfs(0)
    print(*colors, sep='\n')


def __starting_point():
    main()


__starting_point()
