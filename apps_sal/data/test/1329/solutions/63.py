def fact(A):
    c0 = A
    r = 2
    lis = []
    count = 1
    while A != 1:
        if A%r == 0:
            A = A//r
            lis.append(r)
            r = 2
        else:
            r += 1
        if r > int(pow(c0,0.5))+1:
            lis.append(A)
            break
    return(lis)
n = int(input())
lis = []
for i in range(2,n+1):
    lis.extend(fact(i))
lis = sorted(lis)
L = set(lis)
import collections
c = collections.Counter(lis)
x = [0,0,0,0,0]
for R in L:
    if c[R] >= 2:
        x[0] += 1
    if c[R] >= 4:
        x[1] += 1
    if c[R] >= 14:
        x[2] += 1
    if c[R] >= 24:
        x[3] += 1
    if c[R] >= 74:
        x[4] += 1
ans = max((x[0]-2)*(x[1]-1)*x[1]//2, 0) + max((x[1]-1)*x[2], 0) + max((x[0]-1)*x[3], 0) + x[4]
print(ans)
