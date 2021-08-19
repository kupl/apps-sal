# listを並び替えて移動距離の最小値を求める

N = int(input())
a = list(map(int, input().split()))

# 降順に並び替える
descending_a = sorted(a, reverse=True)
# print(descending_a)

# 座標の最大値から最小値を引く→移動距離を求める
print((descending_a[0] - descending_a[-1]))
