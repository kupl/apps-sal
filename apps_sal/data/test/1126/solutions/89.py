import numpy as np


def main():
    n, x, m = list(map(int, input().split()))
    a, r, ans = np.zeros((m + 1), np.int64), 0, 0
    a[0] = x
    for i in range(m):
        tmp = np.power(a[i], 2) % m
        if tmp == 0:
            print((sum(a)))
            return
        r = i + 1
        if tmp in a:
            l = np.where(a == tmp)[0][0]
            ans = sum(a[l:r]) * ((n - l) // (r - l))
            ans += sum(a[l:l + (n - l) % (r - l)])
            break
        a[r] = tmp
    print((ans + sum(a[:l])))


def __starting_point():
    main()


__starting_point()
