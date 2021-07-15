n,k = list(map(int,input().split()))

A = [int(x) for x in input().split()]
A.sort()
median = A[n//2]

inf = 10**16

from collections import defaultdict as dd, deque
C = dd(int)
for x in A[n//2:]:
    C[x] += 1
C[inf] = 123

nmedian = C[median]

S = sorted(C.items())

i = 0
while i < len(S) and S[i][0] < median:
    i += 1

while True:
    who,count = S[i+1]

    afford = k//nmedian
    if who != inf:
        can =  who - median
    else:
        can = inf

    if min(afford,can) == can:
        k -= can*nmedian
        median = who
        nmedian += count
    else:
        median += afford
        break
    i += 1
print(median)



