N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

ord = [-1 for _ in range(N)]
ord[0] = 0
v = A[0]-1
root = [0]

while ord[v] == -1:
    #ordに何回目のワープかが記録される
    ord[v] = len(root)
        #ワープの軌跡を記録
    root.append(v)

    #次の地点にワープ5
    v = A[v]-1

# print(ord)
# print(root)

#ord[v]:最終地点（ループ起点 or ループ前の道のり）
# ループ起点までの余分な手
l = ord[v]
#ループ距離
c = len(root) - l

if K < l:
    #ループ前にワープが終了した場合、最終地点を出力
    ans = root[K]
else:
    #ループする回数を計算
    # はじめにループ起点までの余分手をKから引く
    K -= l
    # ループのmodを計算
    K %= c
    # 余分手＋ループのmodの位置の国に止まる
    ans = root[l+K]
print((ans+1))


