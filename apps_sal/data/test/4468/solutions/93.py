from sys import stdin

def main():
    N,T=list(map(int,stdin.readline().strip().split()))
    t=list(map(int,stdin.readline().strip().split()))

    x=0
    for i in range(N-1):
        x+=min(T,t[i+1]-t[i])
    print((x+T))

def __starting_point():
    main()

__starting_point()
