n = int(input())
prices = list(map(int, input().split()))
pr = max(prices)
ind = prices.index(pr)
prices.remove(pr)
spesa = max(prices)
print(ind + 1, spesa)
