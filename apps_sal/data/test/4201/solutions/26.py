h,w,k=map(int,input().split())
m=[[] for _ in range(h)]
for y in range(h):
  m[y]=list(input())

ans=0  
for y in range(1<<h):
  for x in range(1<<w):
    mx,my=[],[]
    for y2 in range(h):
      if y>>y2&1: my.append(y2);
    for x2 in range(w):
      if x>>x2&1: mx.append(x2);
    cnt=0
    for y2 in my:
      for x2 in mx:
        if m[y2][x2]=='#': cnt+=1;
    if cnt==k: ans+=1;
print(ans)
