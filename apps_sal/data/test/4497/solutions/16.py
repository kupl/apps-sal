# -*- coding:utf-8 -*-
N = int(input())

if N == 1:
    print(N)
else:
    for i in range(1, 8):
        if 2**(i + 1) > N:
            print(2**i)
            break
        else:
            i += 1
