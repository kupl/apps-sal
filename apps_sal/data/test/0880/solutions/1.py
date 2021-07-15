import math
n = int(input())

mod = 998244353

F = [1, 1]
f = 1
for i in range(2,n+1):
    f*=i
    f%=mod
    F.append(f)

ret = 1
for i in range(1, n+1):
    ret=ret*i-i+F[i]
    ret%=mod

print(ret)

