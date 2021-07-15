import sys
input = sys.stdin.readline

def main():
    N, K = [int(x) for x in input().split()]

    print((K * (K - 1) ** (N - 1)))

    

def __starting_point():
    main()



__starting_point()
