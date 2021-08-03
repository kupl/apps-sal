def valid(n1, n2, p1, p2, mid):
    x = mid - mid // p1
    y = mid - mid // p2
    rem = mid - mid // (p1 * p2)
    return x < n1 or y < n2 or rem < n1 + n2


def binary_search(n1, n2, p1, p2):
    l, r = 0, 1 << 61
    while (l <= r):
        mid = l + r >> 1
        if (valid(n1, n2, p1, p2, mid)):
            l = mid + 1
        else:
            r = mid - 1
    return l


def main():
    n1, n2, p1, p2 = map(int, input().split())
    print(binary_search(n1, n2, p1, p2))


main()
