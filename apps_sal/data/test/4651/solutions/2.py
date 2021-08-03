q = int(input())
for i in range(q):
    w = int(input())
    e = list(map(int, input().split()))
    r = [1] * w
    for k in range(1, w + 1):
        t = e.index(k)
        while t > 0 and r[t - 1] and e[t] < e[t - 1]:
            if r[t - 1]:
                e[t - 1], e[t] = e[t], e[t - 1]
                r[t - 1] = 0
            t -= 1
    print(*e)
