n=int(input())
i=0
for s in range(n):
    a,b=list(map(int,input().split()))
    
    if (a==b):
        i+=1
    else:
        i=0
    if(i==3):
        break
if(i>=3):
    print("Yes")
else:
    print("No")

