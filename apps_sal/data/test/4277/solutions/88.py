# n:n人
# 電車：1人あたりa円
# タクシー：n人でb円
n, a, b = list(map(int, input().split()))

# 電車の場合
total = n * a

print((min(total, b)))

