
def resolve():
    N = int(input())

    if N % 2 == 1:
        return print(0)

    ans = 0
    tmp = N // 2
    while tmp:
        tmp //= 5
        ans += tmp
    print(ans)


def __starting_point():
    resolve()
__starting_point()
