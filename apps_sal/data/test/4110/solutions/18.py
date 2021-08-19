(d, g) = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]
ans = float('inf')
for i in range(2 ** d):
    score = 0
    cnt = 0
    check = [0] * d
    for j in range(d):
        if i >> j & 1:
            check[j] = 1
            score += (j + 1) * 100 * pc[j][0] + pc[j][1]
            cnt += pc[j][0]
    j = d - 1
    while score < g and j >= 0:
        if check[j] == 0:
            n = min(pc[j][0], -(-(g - score) // ((j + 1) * 100)))
            score += n * (j + 1) * 100
            cnt += n
        j -= 1
    if score >= g:
        ans = min(ans, cnt)
print(ans)
