

def __starting_point():
    r , b = list(map(int,input().split()))
    if r==b:
        print(r,0)
    elif r>b:
        dp = b
        sp = (r-b) // 2
        print(dp,sp)
    else:
        dp = r
        sp = (b-r) // 2
        print(dp,sp)

__starting_point()
