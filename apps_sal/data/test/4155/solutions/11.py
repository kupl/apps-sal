def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

def main(n,h):
    count=0
    hmax=max(h)
    for i in range(hmax):
        j=0
        mizuyari=False
        for j in range(n):
            if h[j]>0:
                if mizuyari==False:
                    mizuyari=True
                    count+=1
                h[j]-=1
            else:
                mizuyari=False
    return count

def __starting_point():
    n,h=readinput()
    ans=main(n,h)
    print(ans)

__starting_point()
