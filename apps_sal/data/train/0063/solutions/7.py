import math


def main():
    (n, k) = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    w = sorted(list(map(int, input().split())))
    sm = 0
    w = list(reversed(w))
    for i in range(k):
        r = a.pop()
        w[k - 1 - i] -= 1
        if w[k - 1 - i] == 0:
            sm += 2 * r
        else:
            sm += r
    o = 0
    for i in range(k):
        if w[i] != 0:
            sm += a[o]
            o += w[i]
    print(sm)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
