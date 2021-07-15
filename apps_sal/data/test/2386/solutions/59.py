import numpy as np
n = int(input())
a = list(map(int, input().split()))
a_ = [abs(a[i]) -  (i+1) for i in range(n)] 
med = int(np.median(a_))

def fun(a, b):
    ans = 0
    for i in range(1, len(a)+1):
        ans += abs(a[i-1]-(b+i))
    return ans

print(fun(a, med))
