n, k = map(int, input().split()) 

import math

ans = 0
for i in range(1, n+1):
    if i < k:
        power = math.ceil(math.log2(k/i))
    else:
        power = 0
    ans += pow(0.5, power)
print(ans / n)
