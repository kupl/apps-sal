import math
from heapq import *


def maxProfit(prices, days):

    payoff = 0
    maxPrice, minPrice = max(prices), min(prices)
    maxIndex, minIndex = prices.index(maxPrice), prices.index(minPrice)
    iterator = iter(prices)
    h = []

    if days == 1:
        print(0)
        return

    for i in range(days):
        p = next(iterator)
        if not i:
            heappush(h, p)
            continue
        if h[0] < p:
            payoff += p - h[0]
            heappop(h)
            heappush(h, p)
        heappush(h, p)

    print(payoff)


def __starting_point():
    n = int(input())
    prices = list(map(int, input().split()))
    maxProfit(prices, n)


__starting_point()
