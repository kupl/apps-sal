N = int(input()) 
A = list(map(int,input().split()))

DP = [(a, -1) for a in A]

for i in range(N):
  for j in range(i+2, N, 2):
    val_nxt = DP[i][0] + A[j]
    if DP[j][0] < val_nxt:
      DP[j] = (val_nxt, i)
    
tmp = -10**20
i_max = -1
for j, dp in enumerate(DP):
  if dp[0] > tmp:
    tmp = dp[0]
    i_max = j
print(tmp)
#print(DP)
#print(i_max)
path = []
i = i_max
while i >= 0:
  path.append(i)
  _, i = DP[i]
  
path.reverse()

sft = 0
ans = []
for _ in range(path[0]):
  ans.append(0)
sft += path[0]
for j in range(1,len(path)):
  i_prv = path[j-1]
  d = path[j] - path[j-1]
  for _ in range((d-1)//2):
    ans.append(i_prv+2-sft)
  ans.append(i_prv+1-sft)
  sft += d
for j in range(N-1,path[-1],-1):
  ans.append(j-sft)
#print(path)    

ans = [a+1 for a in ans]
print(len(ans))
print(*ans, sep="\n")
  
  
