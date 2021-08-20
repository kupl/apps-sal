t = int(input())
for _ in range(t):
    (n, _) = list(map(int, input().split()))
    ks = list(map(int, input().split()))
    s = set()
    c = 0
    while len(s) < n:
        for k in ks:
            if k - c > 0:
                s.add(k - c)
            if k + c <= n:
                s.add(k + c)
        c += 1
    print(c)
