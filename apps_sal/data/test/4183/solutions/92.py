N = int(input())
T = [int(input()) for i in range(N)]
import math
a = T[0]
for i in range(1,N):
    a = (a*T[i]) // math.gcd(a,T[i])
print(a)
