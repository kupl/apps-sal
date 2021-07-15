H,W=list(map(int,input().split()))
l=[list(input()) for i in range(H)]
ans_l=[[0]*W for i in range(H)]
for i in range(H):
   for j in range(W):
      if l[i][j] == ".":
         tmp=0
         for x in range(max(0,j-1),min(W-1,j+1)+1):
            for y in range(max(0,i-1),min(H-1,i+1)+1):
               if l[y][x]=="#":
                  tmp+=1
         ans_l[i][j]=str(tmp)
      else:
         ans_l[i][j]="#"
for i in ans_l:
   print(*i,sep="")
