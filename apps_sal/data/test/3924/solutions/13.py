import math
n,k=map(int,input().split(" "))
plan=list(input().split())
plan=[int(x) for x in plan]
count=0
temp=0
for i in range(len(plan)):
    if i==n-1:
        if temp==0:
            count+=math.ceil(plan[i]/k)
            break
        else:
            plan[i]-=(k-temp)
            count+=1
            temp=0
            if plan[i]<0:
                plan[i]=0
            count+=math.ceil(plan[i]/k)
            break
    if temp!=0:
        plan[i]-=(k-temp)
        count+=1
        temp=0
        if plan[i]<0:
            plan[i]=0
    count+=int(plan[i]/k)
    temp=plan[i]%k
print(int(count))
