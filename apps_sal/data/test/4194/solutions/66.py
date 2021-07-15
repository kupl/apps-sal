def readinput():
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,m,a

def main(n,m,a):
    days=sum(a)
    if days>n:
        return -1
    else:
        return n-days

def __starting_point():
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)

__starting_point()
