import math


def binsearch(l, r, fn):
    while r - l > 1:
        m = (l + r) // 2
        if fn(m):
            l = m
        else:
            r = m
    return l


def main():
    (N, A, B) = list(map(int, input().split()))
    l = []
    C = A - B
    for _ in range(N):
        h = int(input())
        l.append(h)

    def func(i):
        if max(l) <= B * i:
            return False
        r = 0
        for j in l:
            r += max(math.ceil((j - B * i) / C), 0)
        if r <= i:
            return False
        return True
    return 1 + binsearch(0, 1000000000, func)


print(main())
