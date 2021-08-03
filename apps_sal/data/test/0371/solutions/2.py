def main():
    m = int(input())
    if m < 1000000:
        lo = m * 4
        hi = m * 8
    else:
        lo = int(4.949 * m)
        hi = int(4.9492 * m)
    while lo < hi - 1:
        mid = (lo + hi) // 2
        nposs = countposs(mid)
        if nposs < m:
            lo = mid
        else:
            hi = mid
    if m == countposs(hi):
        print(hi)
    else:
        print(-1)


def countposs(maxtake):
    k = 2
    ans = 0
    while True:
        term = maxtake // (k * k * k)
        if term == 0:
            return ans
        ans += term
        k += 1


main()
