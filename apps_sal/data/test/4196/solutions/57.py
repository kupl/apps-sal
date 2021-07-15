import math
from collections import deque
N = int(input())
A = list(map(int,input().split()))

M = 0
L = deque([0])
R = deque([0])
for i in range(1,N+1):
    L.append(math.gcd(L[-1],A[i-1]))
    R.appendleft(math.gcd(R[0],A[N-i]))
for j in range(N):
    m = math.gcd(L[j],R[j+1])
    M = max(M,m)
print(M)
