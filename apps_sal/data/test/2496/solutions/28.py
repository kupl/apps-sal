from functools import reduce
from math import gcd

N = int(input())
A = list(map(int, input().split()))

c = max(A) + 1
D = [0] * c
div = [0] * c
P = []

for i in range(2, c):
    if D[i] == 0:
        P.append(i)
        D[i] = i
    for j in P:
        if i * j >= c or j > D[i]:
            break
        D[i * j] = j
f = 0
for i in A:
    if i == 1:
        continue
    temp = i
    while temp != 1:
        if div[D[temp]] == 1:
            f = 1
            break
        div[D[temp]] += 1
        temp2 = D[temp]
        while temp % temp2 == 0 and temp >= temp2:
            temp = temp // temp2
    if f == 1:
        break

if f == 0:
    print('pairwise coprime')

elif reduce(gcd, A) == 1:
    print('setwise coprime')

else:
    print('not coprime')
