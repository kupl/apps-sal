mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    aa = input().rstrip('\n')
    ab = input().rstrip('\n')
    ba = input().rstrip('\n')
    bb = input().rstrip('\n')

    if N <= 3:
        print((1))
        return

    if ab == "A":
        if aa == "A":
            print((1))
        else:
            if ba == "A":
                dp_a = [0] * N
                dp_b = [0] * N
                dp_a[0] = 1
                for i in range(1, N - 1):
                    dp_a[i] = (dp_a[i - 1] + dp_b[i - 1]) % mod
                    dp_b[i] = dp_a[i - 1]
                print((dp_a[N - 2]))
            else:
                print((pow(2, N - 3, mod)))
    else:
        if bb == "B":
            print((1))
        else:
            if ba == "B":
                dp_a = [0] * N
                dp_b = [0] * N
                dp_a[0] = 1
                for i in range(1, N - 1):
                    dp_a[i] = (dp_a[i - 1] + dp_b[i - 1]) % mod
                    dp_b[i] = dp_a[i - 1]
                print((dp_a[N - 2]))
            else:
                print((pow(2, N - 3, mod)))


def __starting_point():
    main()


__starting_point()
