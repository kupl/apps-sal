def main():

    N = int(input())

    ans = 0

    for i in range(1,N+1):
        n_max = int(N/i)
        ans += n_max*(n_max+1)*i

    print((int(ans/2)))

def __starting_point():
    main()

__starting_point()
