import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()

def main():

    """
    <UnionFindを使わない別解>

    x方向とy方向に分けて頂点を辺だと思うのは定石？？？（確かに長方形がメインなら直積分解したくなる？）
    このとき問題文は「長さ３のパスがあればパスを１本追加する操作を繰り返して、各連結成分を完全二部グラフにせよ」

    完全二部グラフになるのは背理法からすぐわかる。なので解法は(¥Sum_{i:component}X_i Y_i) - N
    """

    N = int(input())
    V = 10 ** 5 + 1 # padding for y
    repn = [[] for _ in range(V * 2)]
    for _ in range(N):
        x, y = list(map(int, input().split()))
        repn[x].append(V + y)
        repn[V + y].append(x)

    visited = [0] * (V * 2)
    count = [0, 0]

    # dfsでその都度連結成分を求める
    def dfs(v):
        if visited[v]:
            return
        visited[v] = 1
        count[v // V] += 1
        for u in repn[v]:
            dfs(u)

    ans = 0
    for i in range(V * 2):
        if visited[i]:
            continue
        count[:] = [0, 0]
        dfs(i)
        ans += count[0] * count[1]
    print((ans - N))


def __starting_point():
    main()

__starting_point()
