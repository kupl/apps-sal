
def main():
    D, N = list(map(int, input().split()))
    if D == 0:
        if N <= 99:
            print(N)
        else:
            print((N+1))
    elif D == 1:
        if N <= 99:
            print((100*N))
        else:
            print((101*N))
    else:
        if N <= 99:
            print((10000*N))
        else:
            print((10100*N))

def __starting_point():
    main()

__starting_point()
