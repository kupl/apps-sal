a, b, c = map(int, input().split())
min_price = min(a + b, b + c, a + c)
print(min_price)
