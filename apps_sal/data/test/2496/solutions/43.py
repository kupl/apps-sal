from math import gcd
flag = 0
N = int(input())
A = list(map(int, input().split()))
Max = max(A)
a = [0] * (Max + 1)
for i in A:
    a[i] += 1
for i in range(2, Max + 1):
    if sum(a[i::i]) >= 2:
        flag = 1
        break
if flag == 0:
    print('pairwise coprime')
else:
    r = A[0]
    for i in A:
        r = gcd(r, i)
    if r == 1:
        print('setwise coprime')
    else:
        print('not coprime')
