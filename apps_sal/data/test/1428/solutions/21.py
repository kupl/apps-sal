# # coding: utf-8
# # Your code here!

# //解説
# #include <iostream>
# #define rep(i,n) for(int i=0;i<n;i++)
# using namespace std;
# int N,C,X;
# int D[33][33];
# int t[3][33];
# int main(void)
# {
#     scanf("%d%d",&N,&C);
#     rep(i,C)rep(j,C)scanf("%d",&D[i][j]);
#     rep(i,N)rep(j,N)scanf("%d",&X),t[(i+j)%3][X-1]++;
#     int res=1<<30;
#     rep(i,C)rep(j,C)if(i!=j)rep(k,C)if(i!=k&&j!=k)
#     {
#         int tt=0;
#         rep(l,C)tt+=D[l][i]*t[0][l];
#         rep(l,C)tt+=D[l][j]*t[1][l];
#         rep(l,C)tt+=D[l][k]*t[2][l];
#         if(tt<res)res=tt;
#     }
#     printf("%d\n",res);
# }


from collections import defaultdict
N,C=list(map(int,input().split()))
D=defaultdict(int)
t=defaultdict(int)

for i in range(C):
    s=list(map(int,input().split()))
    for j in range(C):
        D[(i,j)]=s[j]
for i in range(N):
    s=list(map(int,input().split()))
    for j in range(N):
        t[((i+j)%3,s[j]-1)]+=1
ans=1<<30
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i!=j!=k!=i:
                res=0
                for l in range(C):res+=D[(l,i)]*t[(0,l)]
                for l in range(C):res+=D[(l,j)]*t[(1,l)]
                for l in range(C):res+=D[(l,k)]*t[(2,l)]
                ans=min(ans,res)

                
print(ans)
                


