from math import sqrt, ceil


def main():
    (n, a, b) = [int(i) for i in input().split()]
    swaped = 0
    if a > b:
        (a, b) = (b, a)
        swaped = 1
    if a * b >= 6 * n:
        print(a * b)
        print(a, b)
        return 0
    new_a_max = ceil(sqrt(6 * n))
    ans = []
    for newa in range(a, new_a_max + 1):
        newb = ceil(6 * n / newa)
        if newa * newb >= 6 * n and newb >= b:
            ans.append([newa * newb, newa, newb])
    ans = sorted(ans)
    if swaped:
        (ans[0][1], ans[0][2]) = (ans[0][2], ans[0][1])
    print(ans[0][0])
    print(ans[0][1], ans[0][2])


def __starting_point():
    main()


__starting_point()
