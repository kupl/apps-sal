N, M = map(int, input().split())
l = []
for i in range(N):
  l.append(list(map(int, input().split())))
  
ans = [0] * (M+1)
for i in range(N):
  n = l[i]
  for j in range(1, n[0]+1):
    ans[n[j]] += 1
    
cnt = 0
for i in range(M+1):
  if ans[i] == N:
    cnt += 1
print(cnt)
