'''
Created on 2019/09/23

@author: oiwaiman
'''


import numpy as np

n = int(input())
aaa = np.fromiter(list(map(int, input().split())), np.int64)

all_x = np.bitwise_xor.reduce(aaa)

mask = ~all_x
bbb = aaa & mask

ans = 0
while True:
    a = bbb.max()
    if a == 0:
        break
    b = 1<<(int(a).bit_length() -1)
    bbb[bbb & b > 0] ^= a
    if ans & b == 0:
        ans ^= a


print (ans*2 + all_x)
