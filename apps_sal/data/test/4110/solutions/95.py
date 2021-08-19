d, g = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]

ans = float("inf")

for bit in range(1 << d):
    count = 0
    sum = 0
    nokori = set(range(1, d + 1))

    for i in range(d):
        if bit & (1 << i):
            sum += pc[i][0] * (i + 1) * 100 + pc[i][1]
            count += pc[i][0]
            nokori.discard(i + 1)

    # G 点に満たなければ nokori のうち一番大きいものを解く
    if sum < g:
        use = max(nokori)
        n = min(pc[use - 1][0], -(-(g - sum) // (use * 100)))
        count += n
        sum += n * use * 100

    if sum >= g:
        ans = min(ans, count)

print(ans)
