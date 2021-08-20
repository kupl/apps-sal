for _ in range(int(input())):
    k = int(input())
    days = list(map(int, input().strip().split()))
    sd = sum(days)
    ans = 0
    if k > sd:
        t = k // sd
        ans += t * 7
        k = k % sd
    if k == 0:
        k += sd
        ans -= 7
    ways = [days[start:] + days[:start] for start in range(7)]
    minw = 7
    for way in ways:
        sk = k
        d = 0
        for v in way:
            sk -= v
            d += 1
            if sk == 0:
                break
        if minw > d:
            minw = d
    ans += minw
    print(ans)
