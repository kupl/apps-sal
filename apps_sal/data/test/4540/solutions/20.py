N = int(input())
A = [0] + list(map(int,input().split())) + [0]
B = [0] * (N+1)
total = 0
for i in range(N+1):
    B[i] = A[i+1]-A[i]
    total += abs(B[i])
for i in range(N):
    print((total - (abs(B[i])+abs(B[i+1])) + abs(B[i]+B[i+1])))

