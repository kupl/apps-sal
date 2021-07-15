n=int(input())
a=list(map(int,input().split()))
color=[]
count,free=0,0

for i in range(n):
    c=a[i]//400
    if a[i]<3200 and c not in color:
        color.append(c)
        count+=1
    elif a[i]>=3200:
        free+=1
      
min,max=0,0
if count==0:
    max=free
    min=1
else:
    max=count+free
    min=count
    
print(min,max)
