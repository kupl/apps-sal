import math

N = int(input())
T = [int(input())for _ in range(N)]

ans = T[0]

for i in range(1,N):
    ans = (ans*T[i])//math.gcd(ans,T[i])
    #ans %= 10**18+7
print(ans)
    

