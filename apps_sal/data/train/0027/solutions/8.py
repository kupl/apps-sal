for q in range(int(input())):
    n = int(input())
    line = list(map(int, input().split()))
    Q = dict()
    for i in range(n):
        l = 0
        r = 100
        while r - l > 1:
            m = (l + r) // 2
            if line[i] % (1 << m) == 0:
                l = m
            else:
                r = m
        f = line[i] // (1 << l)
        if f in Q:
            Q[f] = max(Q[f], l)
        else:
            Q[f] = l
    Q = list(Q.items())
    ans = 0
    for a, b in Q:
        ans += b
    print(ans)
