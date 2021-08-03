def main():
    M = 10**9 + 7
    r1, c1, r2, c2 = map(int, input().split())
    n = r2 + c2 + 2
    val = 1
    fac = [val]
    append = fac.append
    for i in range(1, n + 1):
        val = val * i % M
        append(val)
    pr1 = pow(fac[r1], M - 2, M)
    pc1 = pow(fac[c1], M - 2, M)
    pr2 = pow(fac[r2 + 1], M - 2, M)
    pc2 = pow(fac[c2 + 1], M - 2, M)
    a = fac[r2 + c2 + 2] * pr2 * pc2
    a -= fac[r2 + c1 + 1] * pr2 * pc1
    a -= fac[r1 + c2 + 1] * pr1 * pc2
    a += fac[r1 + c1] * pr1 * pc1
    print(a % M)


main()
