(n, m) = map(int, input().split())
exams = []
for i in range(m):
    e = list(map(int, input().split()))
    e.append(0)
    e.append(i + 1)
    exams.append(e)
exams.sort()
(now, have, f, ans, c) = (0, [], True, [], 0)
for i in range(1, n + 1):
    while now < m and exams[now][0] == i:
        have.append(exams[now][1:])
        now += 1
        have.sort()
    if c < len(have) and have[c][0] == i:
        if have[c][1] == have[c][2]:
            ans.append(m + 1)
            c += 1
        else:
            f = False
            break
    else:
        j = 0
        while j < len(have) and have[j][1] == have[j][2]:
            j += 1
        if j == len(have):
            ans.append(0)
        else:
            ans.append(have[j][3])
            have[j][2] += 1
if f:
    for i in range(n):
        print(ans[i], end=' ')
else:
    print(-1)
