def readinput():
    n=int(input())
    return n

def main(n):
    ureshii = (n // 500) * 1000
    n = n % 500
    ureshii += (n // 5) * 5
    return ureshii

def __starting_point():
    n=readinput()
    ans=main(n)
    print(ans)

__starting_point()
