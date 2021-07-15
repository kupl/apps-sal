N = int(input())
S = input()

ans = 0
cnt = 0

for i in range(N):
  if S[i] == "I":
    cnt += 1
  elif S[i] == "D":
    cnt -= 1
  
  ans = max(ans, cnt)
  
print(ans)
