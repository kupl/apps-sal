import sys
import math
n, k = map(int, input().split())
x = (k * (k + 1)) // 2
cur = 1
s = math.sqrt(n)
div = 0
while(cur <= s):
    if(n % cur == 0):
        if(n // cur >= x):
            div = max(div, cur)
        if(cur >= x):
            div = max(div, n // cur)
    cur += 1
if(div == 0):
    print(-1)
    return
rest = n // div
for i in range(1, k + 1):
    if(i == k):
        print(div * rest, end=' ')
    else:
        print(div * i, end=' ')
    rest -= i
