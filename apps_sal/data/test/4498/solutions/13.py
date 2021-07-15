def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c, d = Input()

    if abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d):
        print("Yes")
    else:
        print("No")


main()
