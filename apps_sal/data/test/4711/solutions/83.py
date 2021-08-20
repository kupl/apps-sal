(a, b, c) = map(int, input().split())
prices = [a + b, a + c, b + c]
print(min(prices))
