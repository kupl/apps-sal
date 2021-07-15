import math
from functools import reduce

def getD(num):
    input_list = [2 if i % 2 == 0 else i for i in range(num+1)]
    input_list[0] = 0
    bool_list = [False if i % 2 == 0 else True for i in range(num+1)]
    sqrt = int(math.sqrt(num))
    
    for serial in range(3, sqrt + 1, 2):
        if bool_list[serial]:
            for s in range(serial ** 2, num+1, serial):
                if bool_list[s]:
                    input_list[s] = serial
                    bool_list[s] = False
    return input_list

N = int(input())
A = list(map(int, input().split()))

D = getD(max(A))
pairwise_coprime = True
use_divnum = set()
for i in range(N):
    k = A[i]
    while k != 1:
        if D[k] in use_divnum:
            pairwise_coprime = False
            break
        else:
            use_divnum.add(D[k])
        div = D[k]
        while k % div == 0 and k > 1:
            k = k // div
if pairwise_coprime: 
    print("pairwise coprime")
    return
from math import gcd
gcd_of_a = A[0]
for i in range(N):
    gcd_of_a = gcd(gcd_of_a, A[i])
if gcd_of_a == 1:
    print("setwise coprime")
else:
    print("not coprime")

