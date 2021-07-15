def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, m, x = Input()
    a = [0] * n
    for i in Input():
        a[i-1] = 1

    print(min(sum(a[:x]), sum(a[x-1:])))


main()
