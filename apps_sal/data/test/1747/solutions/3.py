def main():
    (n, k) = list(map(int, input().split()))
    (l, cnt) = (list(map(int, input().split())), [0] * 1000001)
    start = end = j = m = 0
    for (i, x) in enumerate(l):
        if not cnt[x]:
            k -= 1
        cnt[x] += 1
        if k < 0:
            x = l[j]
            cnt[x] -= 1
            if not cnt[x]:
                k += 1
            j += 1
        if m < i - j:
            (m, start, end) = (i - j, j, i)
    print(start + 1, end + 1)


def __starting_point():
    main()


__starting_point()
