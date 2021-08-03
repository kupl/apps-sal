def main():
    m = int(input())
    lo = m * 4
    hi = m * 8
    loposs = countposs(lo)
    hiposs = countposs(hi)
    while lo < hi - 1:
        if hi - lo > 10000:
            mid = lo + int((m - loposs) / (hiposs - loposs) * (hi - lo))
            mid = max(lo + 1, min(hi - 1, mid))
        else:
            mid = (hi + lo) // 2
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
