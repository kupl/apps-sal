import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
mod = 10**9+7
A = [0]*(N+1)
SA = [0]*(N+1)

A[1] = N
SA[1] = N
if N >= 2:
    A[2] = N**2
    SA[2] = N+N**2

for i in range(3,N+1):
    A[i] = A[i-1]+SA[i-3]+(N-i+2)+(N-1)**2
    A[i] %= mod
    SA[i] = SA[i-1]+A[i]
    SA[i] %= mod

print((A[-1]))

