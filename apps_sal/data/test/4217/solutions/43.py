N, M = [int(x) for x in input().split()]
Like = [0 for _ in range(M+1)]
for i in range(N):
  KA = [int(x) for x in input().split()]
  for j in range(1, KA[0]+1):
    Like[KA[j]] += 1
ans = 0
for i in range(M+1):
  if(Like[i]==N):
    ans += 1
print(ans)
