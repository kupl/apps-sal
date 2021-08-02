a, b, c = map(int, input().split())
total_price = min(a + b, a + c, b + c)
print(total_price)
