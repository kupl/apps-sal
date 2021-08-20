from math import inf


def main():
    n = int(input())
    l = -inf
    r = inf
    for i in range(n):
        (c, d) = list(map(int, input().split()))
        if d == 1:
            l = max(1900, l)
        else:
            r = min(1899, r)
        if l > r:
            print('Impossible')
            return
        l += c
        r += c
    if r == inf:
        print('Infinity')
    else:
        print(r)


main()
