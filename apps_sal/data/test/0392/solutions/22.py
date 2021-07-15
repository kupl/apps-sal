import math
from sys import stdin, stdout

def check(k):
    i = 2
    i2 = i*i
    while i2 <= k:
        if k % i2 == 0:
            return False
        i += 1
        i2 = i*i
        
    return True

line = stdin.readline()
n = int(line)

ans = 0
sq_n = int(math.sqrt(n))
i = 1
while i <= sq_n:
    if n % i != 0:
        i += 1
        continue

    if check(i) == True:
        ans = max(ans, i)

    j = int(n / i)
    if check(j) == True:
        ans = max(ans, j)
    i += 1

print(ans)

