
def main():

    N = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    n = N // 2
    print((d[n] - d[n-1]))

def __starting_point():
    main()


__starting_point()
