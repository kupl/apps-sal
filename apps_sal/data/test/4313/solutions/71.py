n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
Ans = 0

for i in range(n):
    if V[i] > C[i]:
        Ans += V[i] - C[i]
print(Ans)
