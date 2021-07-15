import math
N = int(input())
lsa = list(map(int,input().split()))
lcm = lsa[0]
for i in range(1,N):
    lcm = lcm*lsa[i]//math.gcd(lcm,lsa[i])
m = lcm-1
ans = 0
for i in range(N):
    ans += m % lsa[i]
print(ans)
