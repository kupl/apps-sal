import math
n = int(input())
for i in range(int(math.sqrt(n)), 0, -1):
    if n % i == 0:
        print(int(i + (n / i) - 2))
        break
