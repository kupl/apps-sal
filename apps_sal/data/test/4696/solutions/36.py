def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    print("Even" if (a * b) % 2 == 0 else "Odd")


main()
