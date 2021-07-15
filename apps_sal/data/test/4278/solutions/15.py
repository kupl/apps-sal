n=int(input())
mozi=[]
for i in range(n):
    mozi.append(sorted(input()))
mozi.sort()

def hantei(x,y):
    for i in range(10):
        if x[i]!=y[i]:
            return False
    return True

def conbi(n,r):
    ue=1
    for i in range(n-r+1,n+1):
        ue*=i
 
    sita=1
 
    for i in range(1,r+1):
        sita*=i
 
 
    return (ue//sita)
i=0
ans=0
while i<n-1:
    c=1
    while i<n-1 and hantei(mozi[i],mozi[i+1]):
        c+=1
        i+=1
    ans+=conbi(c,2)
    i+=1

print(ans)
