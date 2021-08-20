def resolve():

    def f(x):
        res = x % 4
        if res == 0:
            return x
        elif res == 1:
            return 1
        elif res == 2:
            return x + 1
        else:
            return 0
    (A, B) = map(int, input().split())
    ans = f(B) ^ f(A - 1)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
