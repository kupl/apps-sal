def main():
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    res = []
    for m in m, m - 1:
        r = c = 0
        cnt = [0] * 400002
        cnt[0] = last = 1
        for a in l:
            if a > m:
                c -= 1
                last -= cnt[c + 1]
            else:
                c += 1
                last += cnt[c]
            r += last
            cnt[c] += 1
            last += 1
        res.append(r)
    print(res[0] - res[1])


def __starting_point():
    main()

__starting_point()
