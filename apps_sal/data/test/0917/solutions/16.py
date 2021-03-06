import sys


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


inf = float('inf')


def main():
    (n, h, m) = get_ints()
    arr = [inf] * n
    for tc in range(m):
        (l, r, x) = get_ints()
        l -= 1
        r -= 1
        for i in range(l, r + 1):
            arr[i] = min(arr[i], x)
    ans = 0
    for i in arr:
        if i == inf:
            ans += h ** 2
        else:
            ans += i ** 2
    print(ans)


def __starting_point():
    main()


__starting_point()
