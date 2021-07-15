# cook your dish here
n=int(input())
l=list(map(int,input().split()))
c=0
mi=0
for i in range(len(l)):
 if l[i]!=0:
  c+=1 
 else:
  if mi<c:
   mi=c 
  c=0
print(max(mi,c))
