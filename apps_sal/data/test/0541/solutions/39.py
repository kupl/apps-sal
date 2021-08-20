def main():
    (n, m) = list(map(int, input().split()))
    brg = []
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        brg.append([a - 1, b - 1])
    brg.sort()
    ans = 1
    (s, e) = brg[0]
    for i in range(1, m):
        (s_, e_) = brg[i]
        if e_ <= e:
            e = e_
        if s_ >= s:
            s = s_
        if e <= s_:
            ans += 1
            s = s_
            e = e_
    print(ans)


def __starting_point():
    main()


__starting_point()
