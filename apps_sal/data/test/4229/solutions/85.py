def readinput():
    n=int(input())
    return n

def main(n):
    ans=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0:
            continue
        else:
            ans+=i
    return ans

def __starting_point():
    n=readinput()
    ans=main(n)
    print(ans)

__starting_point()
