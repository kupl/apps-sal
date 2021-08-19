#!/usr/bin/env python3
# code
N = input()
N_NUMBER = int(N)
N_SUM = sum([int(i) for i in N])

if (N_NUMBER % N_SUM) == 0:
    print('Yes')
else:
    print('No')
