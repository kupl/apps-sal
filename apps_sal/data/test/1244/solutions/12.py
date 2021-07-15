while(1):
    try:
        n=int(input())
        a=list(map(int,input().split()))
        b=[]
        for ele in a:
            if ele in b:
                continue
            else:
                b.append(ele)
        c=1
        for ele in b:
            if a.count(ele)<=(n+1)//2:
                continue
            else:
                c=0
                break
        if c==1:
            print("YES")
        else:
            print("NO")
    
    except EOFError:
        break
