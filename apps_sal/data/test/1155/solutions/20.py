#n = int(input().strip())

n, wanted = list(map(int, input().strip().split()))

prices = []

for market in range(n):
    a, b = list(map(int, input().strip().split()))
    prices.append(a / b)

lowest_price = min(prices)
print(wanted * lowest_price)
