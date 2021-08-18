import sys
input = sys.stdin.readline


def main():
    strings = []
    h, w = map(int, input().split())
    strings = [input().rstrip() for _ in range(h)]
    output = ""

    for i in range(h + 2):
        if i == 0 or i == h + 1:
            igeta = "
            print("{}".format(igeta))
        else:
            output = "
            print(output)


def __starting_point():
    main()


__starting_point()
