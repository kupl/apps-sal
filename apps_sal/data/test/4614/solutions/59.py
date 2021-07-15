def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    abc = sorted(Input())
    if abc[0] == abc[1]:
        print(abc[2])
    else:
        print(abc[0])


main()
