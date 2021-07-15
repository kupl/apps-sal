import sys
input = sys.stdin.readline

l,r=list(map(int,input().split()))

mod=10**9+7
def calc(n):
    NOW=0
    NOWO=0
    NOWE=0

    OE=1
    i=0

    while True:
        if NOW+(1<<i)<=n:
            NOW+=(1<<i)
            if OE==1:
                NOWO+=(1<<i)
            else:
                NOWE+=(1<<i)

            OE=1-OE            
            i+=1

        else:
            if OE==1:
                NOWO+=n-NOW
            else:
                NOWE+=n-NOW

            break

    return (NOWO,NOWE)

O,E=calc(l-1)
SUM0=O**2+(E+1)*E

O,E=calc(r)
SUM1=O**2+(E+1)*E

print((SUM1-SUM0)%mod)


            
        

