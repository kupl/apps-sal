(n, a, b) = map(int, input().split())
train = n * a
taxi = b
min_price = [train, taxi]
print(min(min_price))
