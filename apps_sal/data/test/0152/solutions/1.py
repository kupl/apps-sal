def main():
    def read(): return list(map(int, input().split()))
    n, m, k = read()
    x, s = read()
    a = list(read())
    b = list(read())
    c = list(read())
    d = list(read())
    ans = n * x
    if min(b) <= s:
        Min2 = min(a[i] for i in range(m) if b[i] <= s)
        ans = min(ans, n * Min2)
    b = sorted([(b[i], i) for i in range(m)])
    j = 0
    Min = x
    for i in range(k - 1, -1, -1):
        while j < m and b[j][0] + d[i] <= s:
            Min = min(Min, a[b[j][1]])
            j += 1
        if d[i] > s:
            continue
        cur = (n - c[i]) * Min
        ans = min(ans, cur)
    print(ans)


main()
