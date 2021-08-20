n = int(input())
max_price = 0
prices = []
for _i in range(n):
    price = int(input())
    prices.append(price)
    if max_price < price:
        max_price = price
print(sum(prices) - max_price // 2)
