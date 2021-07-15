t=int(input())
for i in range(t):
    n,x,y,d=list(map(int,input().split()))

    if abs(x-y)%d==0:
        print(abs(x-y)//d)

    else:
        ANS=10**10
        if abs(y-1)%d==0:
            ANS=min(ANS,abs(y-1)//d+(-(-abs(x-1)//d)))

        if abs(n-y)%d==0:
            ANS=min(ANS,abs(y-n)//d+(-(-abs(x-n)//d)))

        if ANS==10**10:
            print(-1)
        else:
            print(ANS)

