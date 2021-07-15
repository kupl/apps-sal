from math import log2
import sys
out = sys.stdout
n = int(input())
if n == 3:
    print(1, 1, 3)
else:
    tmp = n
    current = 1
    while n != 1:
        if n % 2 != 0:
            z = (n//2) + 1
        else:
            z = n//2
        for i in range(z):
            out.write(str(current) + ' ')
        n -= z
        current *= 2
    step = int(log2(tmp))
    if tmp % 2**(step - 1) == 0:
        out.write(str(tmp))
    else:
        q = 2**(step - 1)
        ans = 0
        for i in range(1, 1000):
            if q*i <= tmp:
                ans = max(ans, q*i)
            else:
                break
        out.write(str(ans))
