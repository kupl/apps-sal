A=int(input())
shop_l=[list(map(int,input().split())) for i in range(A)]
shop_count_l=[list(map(int,input().split())) for i in range(A)]
ans=-1*10**10
for i in range(1,1024):
   tmp=0
   l=[0]*A
   for j in range(10):
      if (i>>j)&1:
         for k in range(A):
            if shop_l[k][j] == 1:
               l[k]+=1
   for i in range(A):
      tmp+=shop_count_l[i][l[i]]
   ans=max(ans,tmp)
print(ans)
