def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, k = Input()
    s = input()
    print("".join(ch.lower() if index==k else ch for index, ch in enumerate(s, 1)))


main()
