import math

def main():
    n,m,k,l = map(int, input().strip().split())

    t = int(k + l + m - 1) // m

    if k + l > n:
        print(-1)
        return
    
    if m * t > n:
        print(-1)
        return
    
    print(t)

def __starting_point():
    main()
__starting_point()
