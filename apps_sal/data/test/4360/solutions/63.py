def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def aaa(num):
    return 1 / num


def main():
    n = int(input())
    a = Input()
    ans = 1 / sum((aaa(i) for i in a))
    print(ans)


main()
