import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
x=bisect.bisect_left(a,0)#0以上が何個か調べるため、0が入る位置のインデックス
X=n-x#0以上の個数
#print(x,X)
if a[0]>=0:
    print(a[k-1])
    return
elif a[-1]<=0:
    print(-1*a[-1-k+1])
    return
#右スタート
if X>=k:
    c=0
    for i in range(x,n):
        c+=1
        if c==k:
            ans=a[i]
            j=i
            r=x
            break
    #print(ans,j,r)
    while (j>x and r>0):
        j-=1
        r-=1
        #print(a[j],a[r],j,r)
        ans=min(ans,a[j]*2-a[r])
else:
    c=0
    ans=2*a[-1]
    #print(x,ans)
    for i in range(x-1,-1,-1):
        c+=1
        #print(a[i])
        if c==k-X:
            ans+=-1*a[i]
            j=n-1
            r=i
            break
    #print(ans,j,r)
    while (j>x and r>0):
        j-=1
        r-=1
        #print(a[j],a[r],j,r)
        ans=min(ans,a[j]*2-a[r])
#print(ans)
#print(n-X,k)
#左スタート
#x=bisect.bisect_left(a,0)#0以上が何個か調べるため、0が入る位置のインデックス
#X=n-x#0以上の個数
if n-X>=k:#0以下の個数がkより多い場合
    c=0
    for i in range(x-1,-1,-1):
        c+=1
        #print(i)
        if c==k:
            ans2=-1*a[i]
            j=i
            r=x-1
            break
    #print(ans2,j,r)
    while (j<x-1 and r<n-1):
        j+=1
        r+=1
        #print(a[j],a[r],j,r)
        ans2=min(ans2,-2*a[j]+a[r])
        #print(ans2)
else:
    c=0
    ans2=-2*a[0]
    #print(x,k,ans2,"sss")
    for i in range(x,n):
        c+=1
        #print(a[i],i)
        if c==k-(n-X):
            ans2+=a[i]
            #print(ans2)
            j=0
            r=i
            break
    #print(ans2,j,r)
    while (j<x-1 and r<n-1):
        j+=1
        r+=1
        #print(a[j],a[r],j,r)
        ans2=min(ans2,-2*a[j]+a[r])
#print(ans)
print(min(ans,ans2))
