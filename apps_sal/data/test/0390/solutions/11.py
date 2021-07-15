import sys
n,a,b = map(int,sys.stdin.readline().strip().split())
l = list(map(int,input().split()))
for i in range(n//2):
    if((l[i]==0 and l[n-i-1]==1) or (l[i]==1 and l[n-i-1]==0)):
        print(-1)
        return
ans = 0
for i in range(n//2):
    if(l[i]==1):
        if(l[n-i-1]==2):
            ans+=b
            l[n-i-1] = 1
    elif(l[i]==0):
        if(l[n-i-1]==2):
            ans+=a
            l[n-i-1] = 0
    else:
        if(l[n-i-1]==1):
            ans+=b
            l[i] = 1
        elif(l[n-i-1]==0):
            ans+=a
            l[i] = 0
        else:
            if(a<b):
                l[i] = 0
                l[n-i-1] = 0
            else:
                l[i] = 0
                l[n-i-1] = 0
            ans+=2*min(a,b)
for i in l:
    if(not(i==0 or i==1)):
        ans+=min(a,b)
print(ans)
