def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def calc(i, h):
    return all((h[i] >= h[j] for j in range(i)))


def main():
    n = int(input())
    h = Input()
    ans = 1
    for i in range(1, n):
        ans += calc(i, h)
    print(ans)


main()
