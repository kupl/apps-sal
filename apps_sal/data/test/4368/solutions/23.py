def readinput():
    n,k=list(map(int,input().split()))
    return n,k

def main(n,k):
    keta = 0
    while n > 0:
        keta += 1
        r = n % k
        n = n // k
    return keta

def __starting_point():
    n,k=readinput()
    ans=main(n,k)
    print(ans)

__starting_point()
