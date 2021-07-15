def problemB():
    n, k = list(map(int, input().strip().split()))
    if k == 1:
        print(n)
    else:
        bas = 1
        while n > 0:
            n //=2
            bas *=2
        print(bas-1)


def __starting_point():
    problemB()

__starting_point()
