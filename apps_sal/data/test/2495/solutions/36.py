def main():
    n=int(input())
    a = list(map(int,input().split()))
    sp=0
    sm=0
    cntp=0
    cntm=0
    for i in range(n):
        sp+=a[i]
        sm+=a[i]
        if abs(sp)>=1 and sp//(abs(sp))==(-1)**i:
            sp+=0
        else:
            cntp+=abs(sp)+1
            sp=(-1)**i
        if abs(sm)>=1 and sm//(abs(sm))==(-1)**(i+1):
            sm+=0
        else:
            cntm+=abs(sm)+1
            sm=(-1)**(i+1)
    print((min(cntp,cntm)))
    
def __starting_point():
    main()

__starting_point()
