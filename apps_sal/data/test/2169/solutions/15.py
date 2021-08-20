def main():
    from itertools import accumulate
    (h, w, d) = list(map(int, input().split()))
    a = [0] * (h * w + 1)
    b = [0] * (h * w + 1)
    for i in range(1, h + 1):
        l = list(map(int, input().split()))
        for (j, k) in enumerate(l, 1):
            a[k] = i
            b[k] = j
    c = [0] * (h * w + 1)
    for i in range(d + 1, h * w + 1):
        c[i] = c[i - d] + abs(a[i] - a[i - d]) + abs(b[i] - b[i - d])
    q = int(input())
    res = []
    for _ in range(q):
        (l, r) = list(map(int, input().split()))
        res.append(c[r] - c[l])
    ans = '\n'.join(map(str, res))
    print(ans)


def __starting_point():
    main()


__starting_point()
