N = int(input())
S = list(range(1, N + 1))  # 頂点の数
H = [sorted(list(map(int, input().split()))) for i in range(N - 1)]  # 辺のリスト。頂点は右にいくほど大きい
F = 0
tyouten = int(N * (N + 1) * (N + 2) / 6)
for i in range(len(H)):
    F += H[i][0] * (N - H[i][1] + 1)  # uVの組み合わせによって得られる辺の数をFに追加
print(tyouten - F)  # 頂点数からHselectの要素数を引いた数＝連結成分数
