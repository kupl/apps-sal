price = int(input())
number = int(price / 1000) + 1

if price % 1000 == 0:
    print(0)
else:
    change = number * 1000 - price
    print(change)
