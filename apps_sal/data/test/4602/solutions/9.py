def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (n, k) = (int(input()) for _ in range(2))
    x = Input()
    ans = 0
    for i in range(n):
        ans += min(abs(0 - x[i]), abs(k - x[i])) * 2
    print(ans)


main()
