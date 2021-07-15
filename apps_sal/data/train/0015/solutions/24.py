import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        A, B, X, Y = [int(x) for x in input().split()]
        ma = 0
        ma = max(X * B, ma)
        ma = max(Y * A, ma)
        ma = max((A - X - 1) * B, ma)
        ma = max((B - Y - 1) * A, ma)

        print(ma)


        
        
    

def __starting_point():
    main()



__starting_point()
