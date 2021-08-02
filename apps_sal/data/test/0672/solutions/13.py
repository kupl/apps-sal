def main2(a, b):
    if a == b:
        print("infinity")
        return
    x = a - b
    if b != 0:
        if x // b == 1:
            print(x // b)
            return
        if x // b <= 0:
            print(0)
            return
    xx = [1]
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x //= loop
            xx.extend([loop * j for j in xx if loop * j not in xx])
        else:
            loop += 1
        print(loop, x, xx)
    xx = [k for k in xx if k > b]
    print(len(xx))


def main3(a, b):
    from math import ceil, sqrt
    if a == b:
        print("infinity")
        return
    x = a - b
    if b != 0:
        if x // b == 1:
            print(x // b)
            return
        if x // b <= 0:
            print(0)
            return
    xx = []
    for i in range(b + 1, ceil(sqrt(x))):
        if x % i == 0:
            xx.append(i)
    print(len(xx))


def main(a, b, Test=False):
    from math import ceil, sqrt, floor
    if a == b:
        print("infinity")
        return
    if b > a:
        print("0")
        return
    x = a - b
    ans = 0
    for i in range(1, floor(sqrt(x)) + 1):
        if x % i == 0:
            if i * i == x:
                ans += i > b
            else:
                ans += (i > b) + (x // i > b)
                if Test:
                    print(i, x // i, ans)
    print(ans)


def test():
    from mxn.timer import Timer, timer
    print()
    main(21, 5)
    main(10, 10)
    main(0, 1000)
    with Timer() as tm:
        main(9435152, 272)
    with Timer() as tm:
        main(325508499, 119510657)
    with Timer() as tm:
        main(1000000000, 6)
    main(11, 2, Test=0)
    main(15, 3, Test=1)
# test()


def main_input():
    a, b = list(map(int, input().split()))
    main(a, b)


def __starting_point():
    main_input()


__starting_point()
