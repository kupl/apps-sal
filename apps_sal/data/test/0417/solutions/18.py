from fractions import gcd

# inputa
n, x, d = list(map(int, list(input().split())))

# process
if d == 0:
    if x == 0:
        print((1))
    else:
        print((n + 1))

else:
    # sが何通りあるかを求める

    # dを正にする
    if d < 0:
        d, x = -d, -x

    # d,xを互いに素にする
    g = gcd(d, abs(x))
    d, x = d // g, x // g

    # s=k*x+c*d
    # cは最小で0からk-1の和、最大でn-kからn-1の和
    # kを固定するとs//dは1ずつの単調増加なので、最小と最大で個数が分かる

    # sはs%d=k*x%dなので、それで分類する
    # →klistをk*x%dでソート
    klist = list(range(n + 1))
    klist.sort(key=lambda k: (k * x % d, k))

    # kを固定し、cの最小・最大を求め、加算していく
    ans = 0

    # 1つ前の値を保持
    pmin, pmax = 1, 0
    pmd = -1
    for k in klist:
        # s//dの最小・最大・s%d
        tmin = (k * x + (k - 1) * k // 2 * d) // d
        tmax = (k * x + (2 * n - k - 1) * k // 2 * d) // d
        tmd = k * x % d

        # s%dが前と同じ　かつ
        # s//dの最小<=前の最大　かつ　s//dの最大>=前の最小のとき
        # 最大・最小を更新
        if tmd == pmd and tmin <= pmax and tmax >= pmin:
            pmin, pmax = min(pmin, tmin), max(pmax, tmax)
        else:
            ans += pmax - pmin + 1
            pmin, pmax = tmin, tmax
        pmd = tmd

    ans += pmax - pmin + 1
    print(ans)
