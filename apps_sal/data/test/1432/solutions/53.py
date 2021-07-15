import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

mFR = [0]*(N+1)
for i in range(N):
    mFR[1] += A[i]*((-1)**i)
for i in range(2,N+1):
    mFR[i] = A[i-2]*2-mFR[i-1]
print((*mFR[1:]))

