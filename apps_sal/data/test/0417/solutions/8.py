def LI():
    return list(map(int, input().split()))


(N, X, D) = LI()


def sumeq(n):
    return n * (n + 1) // 2


def main():
    if D == 0:
        if X == 0:
            ans = 1
        else:
            ans = N + 1
        print(ans)
        return
    d = {}
    for i in range(N + 1):
        a = i * X + sumeq(i - 1) * D
        b = sumeq(N - 1) - sumeq(N - i - 1) - sumeq(i - 1)
        v = (a - a % D) // D
        if a % D in d:
            d[a % D].append((v, b))
        else:
            d[a % D] = [(v, b)]
    ans = 0
    for w in list(d.values()):
        w.sort()
        ans += w[0][1] + 1
        x = w[0][0] + w[0][1]
        n = len(w)
        for i in range(1, n):
            r = w[i][0] + w[i][1]
            if x < w[i][0]:
                ans += w[i][1] + 1
            elif x < r:
                ans += r - x
            x = max(x, r)
    print(ans)


def __starting_point():
    main()


__starting_point()
