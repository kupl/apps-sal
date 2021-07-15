N = int(input())

prices = []

for _ in range(N):
    prices.append(int(input()))

prices.append(max(prices) // 2)
prices.remove(max(prices))

print(sum(prices))
