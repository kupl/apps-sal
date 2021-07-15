def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c = Input()
    if a + b >= c:
        print("Yes")
    else:
        print("No")


main()
