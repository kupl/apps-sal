def solve():
    n, m = list(map(int, input().split()))

    while True:
        if n == 0 or m == 0:
            print(n, m)
            return
        elif n >= 2*m:
            n = n % (2*m)
            continue
        elif m >= 2*n:
            m = m % (2*n)
            continue
        else:
            print(n,m)
            return


def __starting_point():
    solve()



__starting_point()
