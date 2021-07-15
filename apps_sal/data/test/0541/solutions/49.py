N,M = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(M)]
ab.sort(key=lambda x: x[1])
ans = 0
pos = 0
for i in range(M):
  if pos<ab[i][0]:
    ans+=1
    pos=ab[i][1]-1
print(ans)
