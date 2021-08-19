s = list(input())
ans = [s[0]]
cnt = 1
if len(s) == 1:
    print(s[0], end='')
    print(1)
else:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans.append(cnt)
            ans.append(s[i + 1])
            cnt = 1
    if s[-1] == s[-2]:
        ans.append(cnt)
    else:
        ans.append(1)
ans2 = [0] * len(s)
sm = 0
for i in range(len(ans) // 2):
    sm += ans[2 * i + 1]
    if ans[i * 2] == 'L':
        if ans[2 * i + 1] % 2 == 1:
            ans2[sm - ans[i * 2 + 1]] += (ans[2 * i + 1] + 1) // 2
            ans2[sm - ans[i * 2 + 1] - 1] += (ans[2 * i + 1] - 1) // 2
        else:
            ans2[sm - ans[i * 2 + 1]] += ans[2 * i + 1] // 2
            ans2[sm - ans[i * 2 + 1] - 1] += ans[2 * i + 1] // 2
    elif ans[2 * i + 1] % 2 == 1:
        ans2[sm - 1] += (ans[2 * i + 1] + 1) // 2
        ans2[sm] += (ans[2 * i + 1] - 1) // 2
    else:
        ans2[sm] += ans[2 * i + 1] // 2
        ans2[sm - 1] += ans[2 * i + 1] // 2
for i in ans2:
    print(i, end=' ')
