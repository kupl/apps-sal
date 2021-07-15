def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, m = Input()
    x = sorted(Input())

    data = sorted((abs(x[i]-x[i+1]) for i in range(m-1)), reverse=True)
    print(sum(data[n-1:]))


main()
