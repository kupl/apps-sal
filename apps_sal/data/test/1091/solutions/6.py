n = int(input())
prices = list(map(int,input().split()))

winner = prices.index(max(prices)) + 1

prices.pop(prices.index(max(prices)))
money = max(prices)
print(winner,money)
