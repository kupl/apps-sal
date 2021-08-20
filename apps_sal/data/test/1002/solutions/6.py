(n, d) = [int(c) for c in input().split()]
t = sum([int(c) for c in input().split()])
breaks = (n - 1) * 10
if t + breaks > d:
    print(-1)
else:
    free = d - (t + breaks)
    print(2 * (n - 1) + free // 5)
