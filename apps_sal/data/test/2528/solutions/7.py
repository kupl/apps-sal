# cook your dish here
n=int(input())
lst=list(map(int,input().split()))
count=0
flag=0
l=[]
for item in lst:
 if item!=0:
  count+=1 
 else:
  l.append(count)
  count=0
l.append(count)
print(max(l))
 

