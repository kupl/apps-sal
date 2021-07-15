def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def func(i, k):
    count = 0
    while i < k:
        i *= 2
        count += 1
    return count


def main():
    n, k = Input()
    ans = 0
    for i in range(1, n+1):
        ans += 1/n * (1/2 ** func(i, k))
    print(ans)


main()
