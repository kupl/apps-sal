import math
n = int(input())
aupper = int(math.sqrt(n))
for a in range(aupper, 0, -1):
    if n % a == 0:
        print(a, int(n / a))
        break
