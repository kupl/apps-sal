from math import *

for zz in range(int(input())):
    n = int(input())
    cp = 10
    ans = []
    while n > 0:
        t = (n % cp) - n % (cp // 10)
        if t > 0:
            ans.append(t)
        n -= t
        cp *= 10

    print(len(ans))
    print(*ans)
