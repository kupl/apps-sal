t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    mx = max(a)
    sols = []
    if mx < n:
        l1 = list(sorted(a[:mx]))
        l2 = list(sorted(a[mx:]))
        rl1 = list(range(1, mx+1))
        rl2 = list(range(1, n-mx+1))
        if l1 == rl1 and l2 == rl2:
            sols.append((mx, n - mx))
        l1 = list(sorted(a[:n-mx]))
        l2 = list(sorted(a[n-mx:]))
        if mx*2 != n and l1 == rl2 and l2 == rl1:
            sols.append((n-mx, mx))
    print(len(sols))
    for p in sols:
        print(*p)

