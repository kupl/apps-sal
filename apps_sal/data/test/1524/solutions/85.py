S = input()
N = len(S)
ans = [1]*N
 
for i in range(N-1):
  if S[i] == S[i+1] == "R":
    ans[i+2] += ans[i]
    ans[i] = 0
    
for j in range(N-1,0,-1):
  if S[j] == S[j-1] == "L":
    ans[j-2] += ans[j]
    ans[j] = 0
    
print(*ans)
