import bisect
n_shops = int(input())
prices = [int(x) for x in input().split(' ')]
prices.sort()
n_days = int(input())
for day in range(n_days):
    coins = int(input())
    N = bisect.bisect(prices, coins)
    print(N)
