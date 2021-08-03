
def __starting_point():
    n, m, k = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    ans = 0
    for start in range(m):
        ac = aa[:]
        for i in range(start, n, m):
            ac[i] -= k
        cur = 0
        for i in range(start, n):
            if i % m == start:
                cur = max(ac[i] + cur, ac[i])
            else:
                cur += ac[i]
            ans = max(cur, ans)
    print(ans)


__starting_point()
