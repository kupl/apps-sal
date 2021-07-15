N,K=map(int,input().split())
t=[list(map(int,input().split())) for _ in range(N)]
t.sort(key=lambda x:-x[1])
ans=0
dp=set()
p=[]
for i in range(K):
  ans+=t[i][1]
  if t[i][0] in dp:
    p.append(t[i][1])
  dp.add(t[i][0])
ans+=len(dp)**2
wer=ans
while K<N and p:
  if t[K][0] not in dp:
    wer=wer+t[K][1]-p.pop()-len(dp)**2+(len(dp)+1)**2
    ans=max(ans,wer)
    dp.add(t[K][0])
  K+=1
print(ans)
