
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

    A, B = map(int, input().split())

    # 累積和の考えで [0, B] - [0, A-1]
    # 数列を4つ区切りでxorすると0になる
    # 0,1,2,3, -> 00, 01, 10, 11  = 0

    ans = f(B) ^ f(A - 1)
    print(ans)


def __starting_point():
    resolve()
__starting_point()
