def main():
    n,k=map(int,input().split())
    ans=0
    baisuu=n//k
    ans+=baisuu**3
    if k%2==0:
        if baisuu*k+k//2<=n:
            hanbun=baisuu+1
        else:
            hanbun=baisuu
        ans+=hanbun**3
    print(ans)
def __starting_point():
    main()
__starting_point()
