import collections


def main():
    n, z, w = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    # 途中選り好みしても結局a_n - a_n-1になる
    if(n == 1):
        print((abs(w - a[0])))
    else:
        print((max(abs(a[n - 1] - a[n - 2]), abs(a[n - 1] - w))))


def __starting_point():
    main()


__starting_point()
