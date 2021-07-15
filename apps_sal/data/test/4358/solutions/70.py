def readinput():
    n=int(input())
    p=[]
    for _ in range(n):
        p.append(int(input()))
    return n,p

def main(n,p):
    p.sort(reverse=True)
    #print(p)
    p[0]=p[0]//2
    return sum(p)

def __starting_point():
    n,p=readinput()
    ans=main(n,p)
    print(ans)

__starting_point()
