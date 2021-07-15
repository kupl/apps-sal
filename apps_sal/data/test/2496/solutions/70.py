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

flag = True

d_set = set()
for a in A:
    while a != 1:
        d = D[a]
        if d in d_set:
            flag = False
            break
        else:
            d_set.add(d)
        
        while a % d == 0 and a > 1:
            a = a // d

if flag:
    print('pairwise coprime')
    return

if reduce(math.gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')

