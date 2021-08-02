def main():
    n, *a = map(int, open(0).read().split())
    m = n * -~n // 2 + 1 >> 1
    ng = max(a) + 1
    ok = 0
    while ng - ok > 1:
        mid = ok + ng >> 1
        b = [1] + [0] * n * 2
        c = d = s = 0
        for t in a:
            if t >= mid:
                c += 1
                d += b[c] + 1
            else:
                d -= b[c] - 1
                c -= 1
            b[c] += 1
            s += d
        if s >= m: ok = mid
        else: ng = mid
    print(ok)


main()
