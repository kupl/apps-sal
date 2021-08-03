t = int(input())
buf = []
INF = 10 ** 18
for _ in range(t):
    n, k = list(map(int, input().split()))
    base = n - k * (k + 1) // 2
    ans = INF
    l = k + 1

    if base >= 0 and base % l == 0:
        ini = base // l
        if ini <= 9 - k:
            ans = min(ans, ini)
        else:
            tmp = ini - (9 - k)
            tmps = str(9 - k)
            while tmp:
                d = min(9, tmp)
                tmp -= d
                tmps += str(d)
            ans = min(ans, int(tmps[::-1]))

    for d in range(1, 16):
        for i in range(1, l):
            new_base = base + d * 9 * i
            if new_base < 0 or new_base % l != 0:
                continue
            ini = new_base // l
            tmp = ini - 9 * (d - 1) - (10 - (l - i))
            tmps = str(10 - (l - i)) + '9' * (d - 1)
            if tmp < 0:
                continue
            if tmp <= 8:
                tmps += str(tmp)
                ans = min(ans, int(tmps[::-1]))
                continue
            tmp -= 8
            tmps += '8'
            while tmp:
                d = min(9, tmp)
                tmp -= d
                tmps += str(d)
            ans = min(ans, int(tmps[::-1]))

    if ans == INF:
        ans = -1

    buf.append(ans)

print('\n'.join(map(str, buf)))
