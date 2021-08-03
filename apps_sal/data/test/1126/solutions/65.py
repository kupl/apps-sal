def main():
    n, x, m = list(map(int, input().split()))
    a, r = [0] * (m + 1), 0
    chk = [False] * (m + 1)
    a[0] = x
    for i in range(m):
        tmp = pow(a[i], 2, m)
        if tmp == 0:
            print((sum(a)))
            return
        r = i + 1
        if chk[tmp]:
            l = a.index(tmp)
            break
        else:
            chk[tmp] = True
        a[r] = tmp
    print((sum(a[:l]) +
          sum(a[l:r])*((n-l)//(r-l)) +
          sum(a[l :l+(n-l) % (r-l)])))


def __starting_point():
    main()


__starting_point()
