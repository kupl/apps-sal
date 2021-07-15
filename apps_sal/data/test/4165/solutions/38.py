def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    l = sorted(Input())
    x, y = sum(l[:-1]), l[-1]
    print("Yes" if y < x else "No")


main()
