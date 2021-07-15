n, a, b = map(int, input().split())

# 電車の料金
train = n * a
# タクシーの料金　b 円
taxi = b

print(min(train, taxi))
