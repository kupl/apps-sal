def readinput():
    s=int(input())
    return s

def main(s):
    hist=[0]*1000001
    i=1
    n=s
    hist[n]+=1
    while hist[n]<=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        i+=1
        hist[n]+=1
    return i

def __starting_point():
    s=readinput()
    ans=main(s)
    print(ans)

__starting_point()
