n, m = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(m)]

for x in range(1000):
    keta = 1
    nx = x // 10
    d = [x % 10]

    while nx:
        keta += 1
        d.append(nx % 10)
        nx //= 10

    if keta != n:
        continue

    flg = True
    d.reverse()
    for s, c in SC:
        if d[s - 1] != c:
            flg = False
    if flg:
        print(x)
        return

print(-1)
