"""
Created on Tue Sep  8 20:25:36 2020

@author: liang
"""
import math


def Eratosthenes(x):
    lis = [int(i) for i in range(2, x + 1)]
    res = list()
    while lis:
        a = lis.pop(0)
        res.append(a)
        lis = [i for i in lis if i % a != 0]
    return res


X = int(input())
N = int(math.sqrt(X))
lis = Eratosthenes(N)
ans = X
while True:
    if all((ans % i != 0 for i in lis)):
        print(ans)
        break
    ans += 1
