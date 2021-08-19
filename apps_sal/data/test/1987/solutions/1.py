(n, c1, c2) = [int(x) for x in input().split(' ')]
s = input()
cnt = s.count('1')


def price(x):
    return c1 + c2 * (x - 1) ** 2


prices = []
for i in range(1, cnt + 1):
    bigGroupsPeople = n // i + 1
    numBigGroups = n % i
    smallGroupsPeople = n // i
    numSmallGroups = i - n % i
    totalPrice = numBigGroups * price(bigGroupsPeople) + numSmallGroups * price(smallGroupsPeople)
    prices.append(totalPrice)
print(min(prices))
