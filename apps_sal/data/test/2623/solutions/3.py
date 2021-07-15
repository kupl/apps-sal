t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(input())
    s=sorted(s)
    if k==1:
        print(''.join(map(str,s)))
    elif len(set(s))==1:
        print(s[0]*((n+k-1)//k))
    else:
        if len(set(s[:k]))!=1:
            print(s[k-1])
        else:
            tmp=s[0]
            s=s[k:]
            if len(set(s))!=1:
                print(tmp+''.join(map(str,s)))
            else:
                print(tmp+s[0]*((n-k+k-1)//k))
