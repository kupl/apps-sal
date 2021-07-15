n,k,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=[]
found=False
for i in range(m):
    c.append([])
    b.append(0)
for i in a:
    temp=i%m
    b[temp]+=1
    c[temp].append(i)
    if(b[temp]>=k):
        print("Yes")
        found=True
        for j in c[temp]:
            
            print(j,end=' ')
        print()
        break
if(not found):
    print("No")

