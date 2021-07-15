def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, p = Input()
    x = a*3 + p
    ans = x//2
    print(ans)

main()
