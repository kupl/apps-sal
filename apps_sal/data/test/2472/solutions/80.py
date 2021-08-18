import numpy as np
N = int(input())
AB = [''] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))

AB = sorted(AB, key=lambda x: x[1])
total = 0
flag = 1
for i in range(N):
    total += AB[i][0]
    if total > AB[i][1]:
        flag = 0
        break
if flag == 1:
    print('Yes')
else:
    print('No')
