N, K = map(int, input().split())
S = str(input())

ans = 0
for i in range(N-1):
  if S[i] == S[i+1]:
    ans +=1

for i in range(K):
  if N - ans > 2:
    ans += 2
  elif N-ans == 2:
    ans += 1
    break
  else:
    break
    
print(ans)
