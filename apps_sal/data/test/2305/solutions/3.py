import sys
sys.setrecursionlimit(10**6)

N = int(input())  # 頂点数
C = [int(x) - 1 for x in input().split()]  # 頂点の色番号 (1~N) -> (0~N-1)

E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)


def dfs(u, p=-1):

    color = C[u]  # 色番号
    VC[color].append(u)  # 色ごとに stack しておく

    s = 1  # 部分木サイズ（を格納する）
    for v in E[u]:
        if v == p:
            continue

        child[u] = 0  # v の方向にある子孫のうち辿れる頂点の数 = s - 子孫にある、同色を根とする部分木のサイズの合計
        ret = dfs(v, u)

        s += ret  # 純粋な部分木のサイズを計算
        child[u] += ret  # 同色の頂点が切り離されたあとの部分木サイズ

        ans[color] -= child[u] * (child[u] + 1) // 2

    VC[color].pop()
    if VC[color]:  # 上位に同じ色がある場合
        child[VC[color][-1]] -= s  # 一番近い同色から、自分の部分木の大きさをひく
    else:  # 上位に同じ色がない場合
        root_size[color] -= s  # 上位に残っている頂点の数

    return s


child = [0] * N  # 辿っている子の中でのの残り数　とりあえず 0で初期化
root_size = [N] * N  # 根方向に残っている頂点の数（を格納する。操作前は N 全部）
VC = [[] for _ in range(N)]  # 色番号ごと
ans = [N * (N + 1) // 2] * N  # 色ごとの（残りの）組み合わせ数　初期値は 全点の組み合わせ

dfs(0)

for i in range(N):
    print(ans[i] - root_size[i] * (root_size[i] + 1) // 2)
