N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
dif = 0
for i in range(N):
    if V[i] - C[i] >= 0:
        dif += V[i] - C[i]
print(dif)
