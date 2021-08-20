def f(n, x, arr):
    if x == sum(arr) + n - 1:
        print('YES')
    else:
        print('NO')


def __starting_point():
    (n, x) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    f(n, x, arr)


__starting_point()
