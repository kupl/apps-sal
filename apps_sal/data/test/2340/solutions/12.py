for itr in range(int(input())):
    h,o=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a=a[::-1]
    a.pop(-1)
    ans=0
    while h>2:
        if len(a)==0: break
        if h-1==a[-1]:
            if len(a)>1 and h-2==a[-2]: 
                h-=2
                a.pop(-1)
                a.pop(-1)
            else:
                ans+=1
                h-=2
                a.pop(-1)
        else: h=a[-1]+1
    print(ans)
