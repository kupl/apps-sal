(d, g) = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]


def completed(ii):
    return 100 * (ii + 1) * pc[ii][0] + pc[ii][1]


def items(gg, ii):
    return (gg + 100 * (ii + 1) - 1) // (100 * (ii + 1))


count = [0] * 2 ** d
meet = [1] * 2 ** d
for i in range(2 ** d):
    score = 0
    cnt = 0
    for j in range(d):
        if i >> j & 1 == 1:
            score += completed(j)
            cnt += pc[j][0]
    if score >= g:
        count[i] = cnt
        continue
    for j in range(d)[::-1]:
        if ~i >> j & 1 == 1:
            if items(g - score, j) < pc[j][0]:
                tmp = items(g - score, j)
                cnt += tmp
                score += 100 * (j + 1) * tmp
            else:
                cnt += pc[j][0] - 1
                score += 100 * (j + 1) * (pc[j][0] - 1)
        if score >= g:
            count[i] = cnt
            break
    if score < g:
        count[i] = cnt
        meet[i] = 0
ans = sum([pc[s][0] for s in range(d)])
for i in range(2 ** d):
    if meet[i] == 1:
        ans = min(ans, count[i])
print(ans)
