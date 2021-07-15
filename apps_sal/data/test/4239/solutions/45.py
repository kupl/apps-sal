def f(a,x):
    l=[]
    while x!=0:
        l.append(x%a)
        x//=a
    return sum(l)

def main():
    N=int(input())
    MIN=100000
    for k in range(N+1):
        MIN=min(MIN,f(9,k)+f(6,(N-k)))
    return MIN

def __starting_point():
    print(main())
__starting_point()
