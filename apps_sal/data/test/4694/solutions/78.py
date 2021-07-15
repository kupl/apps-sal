N = int(input())
house = list(map(int, input().split()))

# プレゼントを届けるための、最大値から最小値を引いて、最小の移動距離を出力

print(max(house)-min(house))
