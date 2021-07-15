from math import gcd
k=int(input())

cnt=0

for i in range(1,k+1):
    for j in range(1,k+1):
        a=gcd(i,j)
        for k in range(1,k+1):
            cnt+=gcd(a,k)
print(cnt)

