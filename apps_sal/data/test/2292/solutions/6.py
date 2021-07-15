for _ in range(int(input())):
    n=int(input())
    k=n//2
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dicA={}
    dicB={}
    for i in range(k):
        p,q=a[i],a[-i-1]
        if p>q:
            if (q,p) not in dicA:
                dicA[(q,p)]=0
            dicA[(q,p)]+=1
        else:
            if (p,q) not in dicA:
                dicA[(p,q)]=0
            dicA[(p,q)]+=1

    for i in range(k):
        p,q=b[i],b[-i-1]
        if p>q:
            if (q,p) not in dicB:
                dicB[(q,p)]=0
            dicB[(q,p)]+=1
        else:
            if (p,q) not in dicB:
                dicB[(p,q)]=0
            dicB[(p,q)]+=1

    if n%2==1:
        if a[k]!=b[k]:
            print("No")
        else:
            res="Yes"
            for p,q in dicA:
                if (p,q) not in dicB:
                    res="No"
                elif dicA[(p,q)]!=dicB[(p,q)]:
                    res="No"
            print(res)
    else:
        res="Yes"
        for p,q in dicA:
            if (p,q) not in dicB:
                res="No"
            elif dicA[(p,q)]!=dicB[(p,q)]:
                res="No"
        print(res)
