import sys
import math
amount, x, y = [int(s) for s in input().split()]
array = [int(s) for s in input().split()]
counter = 0
if x > y:
    print(amount)
    return
else:
    for i in range(len(array)):
        if array[i] - x <= 0:
            counter += 1
print(math.ceil(counter / 2))
