n=int(input())
a=list(map(int,input().split()))

if(n==1):
    print("YES")
else:
    L={}
    for item in a:
        if(item in L):
            L[item]+=1
        else:
            L[item]=1
    lim=n//2
    if(n%2==1):
        lim+=1
    ans="YES"
    for item in L:
        if(L[item]>lim):
            ans="NO"
    print(ans)

