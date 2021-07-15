import math
import collections
# for z in range(int(input())):
n = int(input())
K = 0
l = 0
r = n + 1
m = 0
while(r - l > 1):
    m = ((l + r) // 2)
    if ((m * (m + 1)) // 2) > n + 1:
        r = m
    else:
        l = m
# for k in range(n):
#     if (k * (k + 1) / 2) > n + 1:
#         break
#     K = k
print((n - l + 1))



