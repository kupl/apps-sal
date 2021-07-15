n=int(input())
s=input()

def count(n,s):
    cntw=0
    cnte=0
    mcntw=0
    mcnte=0
    maxn=0
    for i in range(n):
        if s[i]=="W":
            cntw+=1
        else:
            cnte+=1
        if maxn<cnte-cntw:
            maxn=cnte-cntw
            mcnte=cnte
            mcntw=cntw

    if cntw==0 or cnte==0:
        print((0))
        return

    else:
        print((mcntw+cnte-mcnte))
        return
count(n,s)


