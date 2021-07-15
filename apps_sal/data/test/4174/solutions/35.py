N, X = map(int, input().split())
L = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[i] + L[i])
ans = 0
for j in range(N+1):
  if S[j] <= X:
    ans += 1
print(ans)
