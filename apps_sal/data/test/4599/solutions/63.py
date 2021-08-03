def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a = sorted(Input(), reverse=True)
    alice = bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]

    print(alice - bob)


main()
