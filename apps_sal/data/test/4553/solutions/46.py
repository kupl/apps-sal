def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    s = input()

    if all(chr == "-" if index == a else chr.isdigit() for index, chr in enumerate(s)):
        print("Yes")
    else:
        print("No")


main()
