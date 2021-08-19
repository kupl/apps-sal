def fit(a, m, k, res):
    k1 = k
    for ai in a[-res:]:
        if ai <= k1:
            k1 -= ai
        else:
            k1 = k - ai
            if m == 1:
                return False
            else:
                m -= 1
    return True


def bisect(n, m, k, a):
    (left, right) = (0, n + 1)
    while left + 1 < right:
        middle = (left + right) // 2
        if fit(a, m, k, middle):
            left = middle
        else:
            right = middle
    return left


def main():
    (n, m, k) = list(map(int, input().split()))
    a = tuple(map(int, input().split()))
    print(bisect(n, m, k, a))


main()
