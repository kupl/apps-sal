x = input()
(days, cost) = [int(i) for i in x.split()]
prices = input()
prices = [int(i) for i in prices.split()]
largest = 0
for i in range(0, days - 1):
    diff = prices[i] - prices[i + 1] - cost
    if diff > largest:
        largest = diff
        indexLargest = i
if largest > 0:
    print(largest)
else:
    print('0')
