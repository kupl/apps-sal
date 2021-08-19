def solve(n, m, x, t):
    r = [0] * n
    d = [0] * m
    ans = [0] * m
    cr = 0
    cd = 0
    for i in range(n + m):
        if t[i]:
            d[cd] = x[i]
            cd += 1
        else:
            r[cr] = x[i]
            cr += 1
    cn = 0
    for i in range(m - 1):
        mid = (d[i] + d[i + 1]) // 2
        while cn < n and r[cn] <= mid:
            cn += 1
            ans[i] += 1
    ans[-1] += n - sum(ans)
    return ' '.join((str(i) for i in ans))


def main():
    (n, m) = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]
    print(solve(n, m, x, t))


main()
