import math
import sys
n = int(input())
s = int(input())
root = int(math.ceil(math.sqrt(n)))

buf = 10**12
if s == n:
    print(n + 1)
    return
for i in range(1, root):
    res = s - i
    x = (n - res) // i
    if x * i + res == n and x > 1 and x > res and res >= 0:
        # print(x,i,res,s,n)
        buf = min(buf, x)
# print(buf)
for i in range(2, root + 1):
    count = 0
    b = n
    while(b != 0):
        count += b % i
        b = b // i
    if count == s:
        buf = i
        break
print(buf if buf != 10**12 else -1)
