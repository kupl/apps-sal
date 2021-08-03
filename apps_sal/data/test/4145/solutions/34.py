import math
x = int(input())
if x == 2:
    print(2)
    return
if x % 2 == 0:
    x += 1
for i in range(x, 2 * x, 2):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i)
        break
