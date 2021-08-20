(a, b, c) = list(map(int, input().split()))
price = min(a + b, b + c, a + c)
print(price)
