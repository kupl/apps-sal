from fractions import gcd


def main():

    def fmin(m):
        return X * m + D * m * (m - 1) // 2

    def fmax(m):
        return X * m + D * m * (2 * N - m - 1) // 2
    (N, X, D) = list(map(int, input().split()))
    if D == 0:
        if X == 0:
            print(1)
        else:
            print(N + 1)
        return
    if D < 0:
        (X, D) = (-X, -D)
    if X > 0:
        ans = 0
        g = gcd(X, D)
        loop = D // g
        for d in range(N + 1):
            if loop <= d:
                mmin = max(fmin(d), fmax(d - loop) + D)
            else:
                mmin = fmin(d)
            mmax = fmax(d)
            ans += (mmax - mmin) // D + 1
        print(ans)
    elif X == 0:
        print(fmax(N) // D + 1)
    elif X + D * (N - 1) >= 0:
        ans = 0
        g = gcd(-X, D)
        loop = D // g
        for d in range(N + 1):
            dmax = fmax(d)
            dmin = fmin(d)
            if d < loop:
                ans += (dmax - dmin) // D + 1
            else:
                pmax = fmax(d - loop)
                pmin = fmin(d - loop)
                if pmax < dmax and pmin <= dmin:
                    mmin = max(dmin, pmax + D)
                    ans += (dmax - mmin) // D + 1
                elif pmax >= dmax and pmin > dmin:
                    mmax = min(dmax, pmin - D)
                    ans += (mmax - dmin) // D + 1
                elif pmax < dmax and pmin > dmin:
                    ans += (dmax - pmax) // D + (pmin - dmin) // D
        print(ans)
    else:
        ans = 0
        g = gcd(-X, D)
        loop = D // g
        for d in range(N + 1):
            if loop <= d:
                mmax = min(fmax(d), fmin(d - loop) - D)
            else:
                mmax = fmax(d)
            mmin = fmin(d)
            ans += (mmax - mmin) // D + 1
        print(ans)


def __starting_point():
    main()


__starting_point()
