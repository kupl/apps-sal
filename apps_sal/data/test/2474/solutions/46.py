import numpy as np

n = int(input())
c = np.array(input().split(),dtype=int)
mod = 10**9+7

c = sorted(c)[::-1]
#4^(n-1)を求める
e4 = 1
k = n-1
inst = 4
while k > 0:
    if k%2 == 1:
        e4 = (e4*inst)%mod
    k = k//2
    inst = (inst**2)%mod

ans = 0
for i in range(n):
    ans = (ans+c[i]*(i+2))%mod
ans = (ans*e4)%mod

print(ans)

