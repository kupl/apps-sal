def main():
    (N, M) = list(map(int, input().split()))
    (*A,) = list(map(int, input().split()))
    d = {0: 1}
    ans = 0
    t = 0
    for x in A:
        t = (t + x) % M
        ans += (cnt := d.get(t, 0))
        d[t] = cnt + 1
    print(ans)


def __starting_point():
    main()


__starting_point()
