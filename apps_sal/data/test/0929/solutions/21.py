H,W=list(map(int,input().split()))
l=[list(map(int,input().split())) for i in range(H)]
for i in range(H):
   for j in range(W):
      l[i][j]%=2
sw=0
ans=[]
for i in range(H):
   if i%2==0:
      for j in range(W):
         if sw==1:
            ans.append((i+1,j+1))
         if l[i][j]==1:
            sw=1 if sw==0 else 0
            if sw==1:
               ans.append((i+1,j+1))
            if sw==0:
               ans.append(0)
   else:
      for j in reversed(range(W)):
         if sw==1:
            ans.append((i+1,j+1))
         if l[i][j]==1:
            sw=1 if sw==0 else 0
            if sw==1:
               ans.append((i+1,j+1))
            if sw==0:
               ans.append(0)
f_ans=[]
for i in range(len(ans)-1):
   if ans[i]!=0 and ans[i+1]!=0:
      f_ans.append((*ans[i],*ans[i+1]))
print(len(f_ans))
for i in f_ans:print(*i)
