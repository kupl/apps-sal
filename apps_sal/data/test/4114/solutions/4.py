n=int(input())
xyh = [list(map(int,input().split())) for i in range(n)]
xyh.sort(key=lambda x:x[2], reverse=True)

ansh=-1
ans=[[]]
flag=True
for cx in range(0,101):
  if flag==False:
    break
    
  for cy in range(0,101):
    ansh = 0
    for pira in xyh:
      if ansh==0:
        ansh=pira[2]+(abs(cx-pira[0])+abs(cy-pira[1]))
        ans[0]=[cx,cy,ansh]
        
      elif len(ans[0])>0 and max(ansh -(abs(cx-pira[0])+abs(cy-pira[1])), 0) != pira[2]:
        ans[0]=[]
    if len(ans[0])>0:
      flag=False
      break
print((*ans[0]))

