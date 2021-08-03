def dif(x):
    return max([b - a for b, a in zip(x[1:], x[:-1])])


def main(n, a):
    mn = dif(a) * 10e10
    for i in range(1, len(a) - 1):
        x = dif(a[:i] + a[i + 1:])
        if x < mn:
            mn = x
        # print(i,x,mn)
    print(mn)


def main_input():
    n = int(input())
    a = [int(i) for i in input().split()]
    main(n, a)


def __starting_point():
    main_input()


__starting_point()
