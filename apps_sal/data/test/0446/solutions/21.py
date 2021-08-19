import math
a = []
for k in range(1, 12):
    a.append((int(math.pow(2, k)) - 1) * int(math.pow(2, k - 1)))
a = a[::-1]
n = int(input())
for i in a:
    if n % i == 0:
        print(i)
        break
