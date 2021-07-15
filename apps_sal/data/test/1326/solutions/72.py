n=int(input())
f=[0]*(n+1)
ans=0
dic={}
for i in range(1,n+1):
  j=n//i
  dic[j]=dic.get(j,0)+i
for key,value in dic.items():
  ans+=value*key*(key+1)//2
print(ans)
