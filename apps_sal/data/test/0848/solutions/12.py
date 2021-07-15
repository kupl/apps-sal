def pair(a,b):
    if a>b:
        return pair(b,a)
    else:
        return (((a + b) * (a + b + 1)) / 2) + b

(n,k)=list(map(int,input().split()))
if k>int((n-1)/2):
    print("-1")
else:
    print(n*k)
    hash={}
    for i in range(1,n+1):
        j=1
        count=0
        while j<=n and count<k:
            if i==j:
                j+=1
                continue
            else:
                p=pair(i,j)
                if p in hash:
                    j+=1
                    continue
                else:
                    hash[p]=1
                    print("%d %d"%(i,j))
                    count+=1
                    j+=1
