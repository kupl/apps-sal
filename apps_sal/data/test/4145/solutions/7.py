"""
Created on Tue Sep  8 20:37:12 2020

@author: liang
"""
import math
X = int(input())
N = int(math.sqrt(X))
lis = list(range(2, N + 1))
ans = X

while True:
    if all(ans % i != 0 for i in lis):
        print(ans)
        break
    ans += 1
