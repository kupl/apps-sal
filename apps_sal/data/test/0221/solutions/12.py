from math import *
n, k = list(map(int, input().split()))
if(k >= n):
    print(1)
    print(1)
else:
    arr = []
    count = ceil(n / (2 * k + 1))
    val1 = n % (2 * k + 1)
    if(val1 >= k + 1 or val1 == 0):
        i = 0
        val = 0
    else:
        i = 1
        val = k + 1 - (k + 1 - val1) + k
        arr.append(k + 1 - (k + 1 - val1))
    while(i < count):
        if(val + k + 1 <= n):
            arr.append(val + k + 1)
        else:
            arr.append(n)
        val += 2 * k + 1
        i += 1
    print(count)
    print(*arr)
