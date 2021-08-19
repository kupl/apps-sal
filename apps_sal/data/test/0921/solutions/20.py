(n, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [(ai + 1) // 2 for ai in a]
r = w - sum(b)
if r < 0:
    print(-1)
else:
    ind = sorted(list(range(n)), key=lambda i: a[i], reverse=True)
    for i in ind:
        c = min(r, a[i] - b[i])
        b[i] += c
        r -= c
        if r == 0:
            break
    print(*b)
