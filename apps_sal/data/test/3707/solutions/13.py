import math


def main():
    n, t, k, d = list(map(int, input().split()))

    if d + t < math.ceil(n / k) * t:
        print("YES")
    else:
        print("NO")


def __starting_point():
    # nonlocal stime
    # stime = time.clock()
    main()


__starting_point()
