def main():
    (n, m, k) = map(int, input().split())
    l = 1
    r = 10 ** 10
    while l + 1 < r:
        med = (l + r) // 2
        cnt = n
        left = max(0, med - 1 - (k - 1))
        right = max(0, med - 1 - (n - k))
        left_cord = max(1, k - med + 1)
        right_cord = min(k + med - 1, n)
        cnt += (k - left_cord + 1) * (left + med - 1) / 2
        cnt += (right_cord - k + 1) * (right + med - 1) / 2
        cnt -= med - 1
        if cnt <= m:
            l = med
        else:
            r = med
    print(l)


main()
