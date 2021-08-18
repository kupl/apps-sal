from math import ceil

d, g = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]

ans = float("inf")
for bit in range(1 << d):
    sum = 0
    cnt = 0
    nokori = set(range(1, d + 1))
    for i in range(d):
        if bit & (1 << i):
            sum += pc[i][0] * 100 * (i + 1) + pc[i][1]
            cnt += pc[i][0]
            nokori.discard(i + 1)

    if sum < g:
        use = max(nokori)
        husoku = min(ceil((g - sum) / (use * 100)), pc[use - 1][0])
        cnt += husoku
        sum += husoku * use * 100

    if sum >= g:
        ans = min(cnt, ans)

print(ans)
