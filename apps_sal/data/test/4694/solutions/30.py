N = int(input())
a = list(map(int, input().split()))

# 一番離れている座標の差
print(max(a) - min(a))
