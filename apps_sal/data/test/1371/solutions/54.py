import sys
amount = int(input())

lst1 = [3, 4, 5]
if amount in lst1:
    print((1))
    return
elif amount < 6:
    print((0))
    return

coins = [x for x in range(3, amount + 1)]

lst = [amount + 1 for x in range(amount + 1)]

lst[0] = 1
lst[1] = 0
lst[2] = 0
lst[3] = 1
lst[4] = 1
lst[5] = 1


for i in range(6, amount + 1):
    counter = 0
    for coin in coins:
        change = i - coin

        if change >= 0:
            counter += lst[change]
    lst[i] = counter

print((lst[-1] % (10**9 + 7)))
