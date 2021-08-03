def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    H, W = Input()
    h, w = Input()
    print(H * W - ((H * w + W * h) - (h * w)))


main()
