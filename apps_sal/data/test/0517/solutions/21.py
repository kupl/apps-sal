n, d, h = map(int, input().split())
if d > h * 2 or (n > 2 and d == 1 and h == 1):
    print(-1)
else:
    ans = []
    for i in range(h):
        ans += [' '.join((str(i + 1), str(i + 2)))]
    t = 1
    for i in range(h + 2, d + 2):
        ans += [' '.join((str(t), str(i)))]
        t = i
    for i in range(d + 2, n + 1):
        ans += [' '.join((str(h), str(i)))]
        t = i
    print('\n'.join(ans))
