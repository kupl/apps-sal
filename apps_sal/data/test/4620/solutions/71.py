import math


def main():
    n = int(input())
    csf = [list(map(int, input().split())) for _ in range(n - 1)]
    for i in range(n):
        if i == n - 1:
            print(0)
        else:
            t = 0
            for c, s, f in csf[i:]:
                t = max(s, t)
                t = math.ceil(t / f) * f + c
                #print("start:", i, t)
            print(t)


def __starting_point():
    main()


__starting_point()
