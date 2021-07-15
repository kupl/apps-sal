import numpy as np
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
A = np.sort(list(map(int,input().split())))
F = np.sort(list(map(int,input().split())))[::-1]
mul = A*F
if K >= sum(A)*N:
    print(0)
    return

ma = 2**40
mi = 0
while ma != mi:
    tgt = (ma + mi)//2
    tmp = np.ceil((mul-tgt)/F)
    num = np.sum(tmp[tmp>0])
    if num <= K:
        ma = mi + (ma - mi)//2
    else:
        mi = mi + (ma - mi)//2+1
print(ma)
