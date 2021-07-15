N, A, B, C = list(map(int, input().split()))
abc = [C, B, A]

l = [0] * N
for i in range(N):
    l[i] = int(input())

import numpy
mpp = 10**10
L = [0] * 3
t = [-10] * 3

for i in range(1, 4**N):
    b = numpy.base_repr(i, 4, N)[-N:]
    L = [A, B, C]
    t = [-10] * 3
    if "1" not in b or "2" not in b or "3" not in b:
        continue
    #print(b)
    for j in range(N):
        for k in range(3):
            if b[j] == str(k + 1):
                L[k] -= l[j]
                t[k] += 10
    mpp = min(mpp, sum(t) + sum([abs(x) for x in L]))

print(mpp)


