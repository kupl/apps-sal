n,k=map(int,input().split())

ar=[-1 for i in range(256)]
ls=list(map(int,input().split()))

for e in ls:
    if ar[e]==-1:
        tmp=max(0,e-k+1)
        for i in range(tmp,e+1):
            if ar[i]!=-1 and ar[i]!=i:
                tmp+=1
                continue
            else:
                while i<=e:
                    ar[i]=tmp
                    i+=1
    print(ar[e],end=" ")

