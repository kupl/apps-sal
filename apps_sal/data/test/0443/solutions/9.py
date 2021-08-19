# python3

def readline(): return list(map(int, input().split()))


def main():
    n, = readline()
    a = tuple(readline())

    if n == 1 or n == 2 and a[0] == a[1]:
        print(-1)
    else:
        print(1)
        print(a.index(min(a)) + 1)


main()
