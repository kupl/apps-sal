(buyers, price) = [int(item) for item in input().split()]
purchases = [input() for _ in range(buyers)]
apples = 0
for purchase in purchases[::-1]:
    if purchase == 'halfplus':
        apples = (apples + 0.5) * 2
    else:
        apples *= 2
print(int((apples - 0.5 * purchases.count('halfplus')) * price))
