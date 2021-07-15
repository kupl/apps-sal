n=int(input())
l=list(map(int,input().split()))
t=int(input())
l.sort()

mx=1
i=0
j=0
count=1
while j<n-1:
    count=1
    i=j+1
    while i<n:
        if l[i]-l[j]<=t:
            count+=1
            i+=1
        else:
            
            break
    if count>mx:
        
        mx=count
    j+=1
            
print(mx)

