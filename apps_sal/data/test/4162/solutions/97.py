import math

N=int(input())
a=list(map(int,input().split()))
lcm=1
for i in range(N):
    lcm=lcm*a[i]//math.gcd(a[i],lcm)

print((sum((lcm-1)%a[i] for i in range(N))))

