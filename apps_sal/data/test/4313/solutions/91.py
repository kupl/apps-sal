N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
total = 0
for i in range(N):
    if V[i] > C[i]:
        total += V[i] - C[i]
print(total)
