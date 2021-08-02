from bisect import bisect_left

t = int(input())

for case in range(t):
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    aa = [e for e, _ in ab]
    aa.sort()
    acc = [0] * (m + 1)
    for i in range(m, 0, -1):
        acc[i - 1] = acc[i] + aa[i - 1]

    if n > m:
        ans = 0
    else:
        ans = sum(aa[-n:])

    for a, b in ab:
        i = bisect_left(aa, b)
        cnt = min(m - i, n)
        sm = acc[m - cnt]
        sm += b * (n - cnt)
        if a < b:
            sm -= b
            sm += a

        ans = max(ans, sm)

    print(ans)

    if case != t - 1:
        input()
