n = int(input())
prices = []
for i in range(0, n):
    prices.append(int(input()))

payment = int(max(prices) / 2 + sum(prices) - max(prices))
print(payment)
