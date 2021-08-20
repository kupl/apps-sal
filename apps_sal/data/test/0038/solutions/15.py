import math
import sys


def main():
    (n, l) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    mask = []
    for i in range(n - 1):
        mask.append(a[i + 1] - a[i])
    mask.append(l - a[n - 1] + a[0])
    b = list(map(int, input().split()))
    path = []
    for i in range(n - 1):
        path.append(b[i + 1] - b[i])
    path.append(l - b[n - 1] + b[0])
    for offset in range(n):
        flag = True
        for i in range(n):
            if mask[(i + offset) % n] != path[i]:
                flag = False
                break
        if flag:
            print('YES')
            return
    print('NO')


def __starting_point():
    main()


__starting_point()
