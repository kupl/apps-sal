N = int(input())
A = [0]+list(map(int,input().split()))+[0]
plan = 0
for i in range(N+1):
    plan += abs(A[i+1]-A[i])
for i in range(N):
    difference = abs(A[i+2]-A[i+1])+abs(A[i+1]-A[i])-abs(A[i+2]-A[i])
    print((plan-difference))

