N,M=map(int,input().split())
A=list(map(int,input().split()))
S=0
dic={}
for i in range(N):
  S+=A[i]
  S=S%M
  if(S not in dic):
    dic[S]=1
  else:
    dic[S]+=1
ans=0
#print(dic)
for k in dic.keys():
  #print(k)
  if(k!=0):
    ans+=dic[k]*(dic[k]-1)//2
  if(k==0):
    ans+=dic[k]+dic[k]*(dic[k]-1)//2
print(ans)
