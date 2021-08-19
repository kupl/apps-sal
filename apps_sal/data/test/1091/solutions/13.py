n = int(input())
prices = [int(x) for x in input().split()]
idx = 0
max_price = prices[0]
pay = 0
for i in range(1, n):
    if prices[i] > max_price:
        pay = max_price
        max_price = prices[i]
        idx = i
    elif prices[i] > pay:
        pay = prices[i]
print(str(idx + 1) + ' ' + str(pay))
