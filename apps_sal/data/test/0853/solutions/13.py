while(1):
    try:
        n=int(input())
        a=list(map(int,input().split()))
        count5=a.count(5)
        count0=a.count(0)
        if count5//9==0 and count0!=0:
            print(0)
        elif  count0==0:
            print(-1)
        else:
            print((count5//9)*9*'5'+count0*'0')
    except EOFError:
        break
        

