N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [V[i] - C[i] for i in range(N)]
ans = 0
for i in range(N):
  if D[i] > 0: ans += D[i]

print(ans)
