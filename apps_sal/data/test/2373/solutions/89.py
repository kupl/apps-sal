N = int(input())
P = list(map(int,input().split()))
for i in range(N):
  if P[i] == i+1:
    P[i] = True
  else:
    P[i] = False
ans = 0
for i in range(N):
  if P[i]:
    ans+=1
    if i+1 < N and P[i+1]:
      P[i+1] = False
print(ans)
