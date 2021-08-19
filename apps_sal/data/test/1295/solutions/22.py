import bisect


def read():
    return [int(x) for x in input().split()]


def main():
    n, m = read()
    a = read()
    b = read()

    res = 0
    for i in range(0, n):
        # cover from left
        cover_left = -1
        bi = bisect.bisect_left(b, a[i])
        if bi != m and b[bi] == a[i]:
            cover_left = 0
        elif bi:
            cover_left = a[i] - b[bi - 1]

        # cover from right
        cover_right = -1
        bi = bisect.bisect_right(b, a[i])
        if bi != m:
            cover_right = b[bi] - a[i]

        if cover_left != -1 and cover_right != -1:
            res = max(res, min(cover_left, cover_right))
        elif cover_right != -1:
            res = max(res, cover_right)
        else:
            res = max(res, cover_left)

    print(res)


main()
