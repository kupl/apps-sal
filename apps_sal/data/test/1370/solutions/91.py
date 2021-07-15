import itertools
 
H,W,K=list(map(int, input().split()))
S=[]
for _ in range(H):
  S.append([int(s) for s in input()])
 
ans=2000
for t in itertools.product([0,1],repeat=H-1):
  cnt=t.count(1)
  lst=[[s for s in S[0]]]
  for h in range(H - 1):
    if t[h]==1:
      lst.append(S[h+1])
    else:
      lst[-1]=[lst[-1][i]+S[h+1][i] for i in range(W)]
  L=len(lst)
  R=[0]*L
  for w in range(W):
    if max(lst[i][w] for i in range(L))>K:
      break
    tmp=[R[i]+lst[i][w] for i in range(L)]
    if max(tmp)>K:
      cnt+=1
      R=[lst[i][w] for i in range(L)]
    else:
      R=tmp
  else:
    ans=min(ans,cnt)
print(ans)

