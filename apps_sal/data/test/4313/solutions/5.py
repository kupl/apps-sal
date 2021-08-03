N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
diff = [0 for i in range(N)]
for i in range(N):
    if V[i] - C[i] > 0:
        ans += V[i] - C[i]
print(ans)
