import math

A, B, C, D = map(int, input().split())

T_kougeki = C / B
A_kougeki = A / D

if math.ceil(T_kougeki) <= math.ceil(A_kougeki): print('Yes')

else:
    print('No')
