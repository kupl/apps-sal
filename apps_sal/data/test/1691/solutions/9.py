l=input().split()
n=int(l[0])
k=int(l[1])
curr=0
ans=1
if(k>n//2):
    k=n-k
for i in range(n):
    curr+=k
    if(i==n-1):
        ans=ans+2*(curr//n)-1
    elif(curr%n<k):
        ans=ans+2*((curr)//n)
    else:
        ans=ans+2*((curr)//n)+1
    print(ans,end=" ")

