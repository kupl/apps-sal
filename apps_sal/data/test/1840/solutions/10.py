def bins(a,k,n1):
 l,h=0,n1-1
 while(l<=h):
  m=(l+h)//2
  if(l==h):
   return m
  elif(a[m][0]<=k):
   l=m+1
  else:
   h=m-1
 return l
n,n1=map(int,input().split())
sp=list(map(int,input().split()))
de=[]
s=0
gosum=[]
for i in range(n1):
 d,g=map(int,input().split())
 de+=[[d,g]]
de.sort()
for i in range(n1):
 s+=de[i][1]
 gosum+=[s]
for i in range(n):
 ind=bins(de,sp[i],n1)
 if(de[ind][0]>sp[i] and ind!=0):
  print(gosum[ind-1],end=" ")
 elif(ind==0 and de[ind][0]>sp[i]):
  print(0,end=" ")
 else:
  print(gosum[ind],end=" ")
 

