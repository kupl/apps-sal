import math
N = int(input())
A = list(map(int, input().split()))
g = math.gcd(A[0],A[1])
for i in range(2,N):
    g = math.gcd(g,A[i])
print(g)    
