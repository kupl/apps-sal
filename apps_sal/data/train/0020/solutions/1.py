for _ in range(int(input())):
    (n, m) = map(int, input().split())
    lm = hm = m
    pt = 0
    ans = 'YES'
    for i in range(n):
        (t, l, h) = map(int, input().split())
        lm -= t - pt
        hm += t - pt
        pt = t
        hm = min(h, hm)
        lm = max(l, lm)
        if hm < lm:
            ans = 'NO'
    print(ans)
