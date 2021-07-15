N=int(input())
P=list(map(int,input().split()))

t = 1
ans = []
for i in range(N):
  if P[i] == t:
    for j in range(i, t-1, -1):
      P[j], P[j-1] = P[j-1], P[j]
      ans.append(j)
    t = i + 1

for i in range(N):
  if i+1 != P[i]:
    print(-1)
    return
if len(ans) == N-1:
  for x in ans:
    print(x)
else:
  print(-1)
