n = int(input())
s=0
l=input().split()

for i in range(n):
    l[i]=int(l[i])
r=0    
for i in range(n-1):
    r=0
    if(l[i]!=0):
        for j in range(i+1,n):
            if(l[i]==l[j]):
                r+=1
        if(r==1):
            s+=1
        elif(r>1):
            print(-1)
            break
if(r<=1):
    print(s)











