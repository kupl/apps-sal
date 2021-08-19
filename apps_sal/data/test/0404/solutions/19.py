# Author:      Divesh Uttamchandani
# Institution: BITS Pilani
import math
n = int(input().strip())
factors = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if(n % i == 0):
        if(i != n // i):
            factors += 2
        else:
            factors += 1
print(factors)
# <> with <3 using Termicoder:
# https://termicoder.github.io
