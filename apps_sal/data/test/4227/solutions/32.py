N, M = [int(a) for a in input().split()]


# iから進める場所をリストにして保管
edges = {i: [] for i in range(1, N + 1)}
for i in range(M):
    a, b = [int(a) for a in input().split()]
    edges[a].append(b)
    edges[b].append(a)


# 深さ優先探索
def search(lst):
    # lst(通過点)の数がN(頂点数)と等しくなったら探索終了（成功）
    if len(lst) == N:
        return 1
    else:
        a = lst[-1]
        # lstの最後尾（現在地）が次に進める場所をnextとしてリスト化
        # nextに以前通った場所が入っていないか確認
        next = [n for n in edges[a] if n not in lst]
        # 次に進める場所がなくなったら探索終了（失敗）
        if len(next) == 0:
            return 0

        tot = 0
        # 再帰でさらに探索
        for n in next:
            tot += search(lst + [n])

        return tot


ans = search([1])

print(ans)
