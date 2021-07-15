n,a,b,c=list(map(int,input().split()))
s=[input() for _ in range(n)]
ans=[]
d={'A':a,'B':b,'C':c}
for i in range(n):
  x,y=list(s[i])
  if d[x]==0 and d[y]==0:
    print('No')
    return
  elif d[x]==1 and d[y]==1 and i<n-1:
    if x in s[i+1]:
      d[x]+=1
      d[y]-=1
      ans.append(x)
    else:
      d[x]-=1
      d[y]+=1
      ans.append(y)
  elif set((d[x],d[y]))==set((1,0)):
    d[x],d[y]=d[y],d[x]
    ans.append(x if d[x]>d[y] else y)
  elif d[x]>=d[y]:
    d[y]+=1
    d[x]-=1
    ans.append(y)
  else:
    d[y]-=1
    d[x]+=1
    ans.append(x)
print('Yes')
for ansi in ans:
  print(ansi)

