
def __starting_point():
    n, k = input().strip().split()
    n = int(n)
    k = int(k)
    a = {}
    for i in range(1, k + 1):
        if n % i in a:
            print('No')
            return
        else:
            a[n % i] = 1
    print('Yes')


__starting_point()
