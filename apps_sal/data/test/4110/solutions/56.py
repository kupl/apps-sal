d, g = map(int, input().split())
pc = list(list(map(int, input().split())) for _ in range(d))
ans = float("inf")

for i in range(1 << d):
    score = 0
    cnt = 0
    nokori = set(range(1, d + 1))

    for j in range(d):
        if i >> j & 1:
            score += (j + 1) * pc[j][0] * 100 + pc[j][1]
            cnt += pc[j][0]
            nokori.discard(j + 1)

    if score < g:
        use = max(nokori)
        n = min(pc[use - 1][0], -(-(g - score) // (use * 100)))  # (g-sum)//(use*100)＞0
        cnt += n
        score += n * use * 100
    if score >= g:
        ans = min(ans, cnt)
print(ans)
