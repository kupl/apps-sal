"""input
3
1 1
2 2
2 12
"""
for _ in range(int(input())):

    def get(n):
        return (4 ** n - 1) // 3
    (n, k) = map(int, input().split())
    if n < 32 and 4 ** n < 1 * 3 * k:
        print('NO')
        continue
    now = 1
    p = 2
    ans = n
    sq = 0
    buff = 0
    d = 4
    while k >= now:
        k -= now
        p *= 2
        now = p - 1
        ans -= 1
        sq = sq * 4 + d - 3
        d *= 2
        if n < 60:
            buff += sq * (4 ** ans - 1) // 3
        else:
            buff = 10 ** 19
        if ans == 0:
            break
    if buff < k:
        print('NO')
    else:
        print('YES', max(ans, 0))
