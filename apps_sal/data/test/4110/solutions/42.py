(D, G) = map(int, input().split())
problem = [list(map(int, input().split())) for _ in range(D)]
ans = 10 ** 15
for i in range(2 ** D):
    score = 0
    prob = 0
    lst = []
    for j in range(D):
        if i >> j & 1:
            score += (j + 1) * 100 * problem[j][0] + problem[j][1]
            prob += problem[j][0]
        else:
            lst.append(j)
    if score < G:
        r = lst[-1]
        for _ in range(problem[r][0] - 1):
            score += 100 * (r + 1)
            prob += 1
            if score >= G:
                break
    if score >= G:
        ans = min(ans, prob)
print(ans)
