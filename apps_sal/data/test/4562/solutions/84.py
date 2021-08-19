import math
n = int(input())
for i in range(10 ** 9):
    if math.sqrt(n) == int(math.sqrt(n)):
        print(n)
        break
    n -= 1
