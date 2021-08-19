# 数値の取得
homecnt = int(input())
homeplace = list(map(int, input().split()))

# 最短距離を計算し出力
dist = max(homeplace) - min(homeplace)
print(dist)
