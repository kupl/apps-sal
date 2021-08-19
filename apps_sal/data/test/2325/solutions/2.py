from array import array
md = 10 ** 9 + 7


def fact_all(N):
    lp = array('Q', [2] * (N + 1))
    pr = array('Q', [2])
    pra = pr.append
    for i in range(3, N + 1, 2):
        if lp[i] == 2:
            lp[i] = i
            pra(i)
        for p in pr:
            ip = i * p
            if p > lp[i] or ip > N:
                break
            lp[ip] = p
    return lp


def cnk(n, k):
    if k > n // 2:
        k = n - k
    ans = 1
    for i in range(n - k + 1, n + 1):
        ans *= i
    for i in range(2, k + 1):
        ans //= i
    ans = ans % md
    return ans


def factor(n, lpa=fact_all(10 ** 6)):
    pws = []
    num_ones = 0
    dv = lpa[n]
    while n > 1 and dv * dv <= n:
        lp = 0
        (c, o) = divmod(n, dv)
        while o == 0:
            lp += 1
            n = c
            (c, o) = divmod(n, dv)
        if lp == 1:
            num_ones += 1
        else:
            pws.append(lp)
        dv = lpa[n]
    if n > 1:
        num_ones += 1
    return (pws, num_ones)


def main():
    q = int(input())
    for __ in range(q):
        (x, y) = input().split()
        (x, y) = (int(x), int(y))
        ans = pow(2, y - 1, md)
        (pws, num_ones) = factor(x)
        for f in pws:
            cm = cnk(f + y - 1, f)
            ans = ans * cm % md
        if num_ones:
            ans = ans * pow(y, num_ones, md) % md
        print(ans)


def __starting_point():
    main()


__starting_point()
