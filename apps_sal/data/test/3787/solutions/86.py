n, a, b = map(int, input().split())

min_b = -((-n) // a)
if not(min_b <= b and a + b <= n + 1):
    print(-1)
    return

ans = []
i = 0
while True:
    tmp = []
    break_flag = False
    for j in range(a):
        if i * a + j >= n:
            break_flag = True
            break
        tmp.append(i * a + j + 1)
    if not tmp:
        break
    ans.append(tmp)
    i += 1
    if break_flag:
        break

ans.sort(reverse=True)
nokori_b = b - len(ans)

for i in range(len(ans) - 1):
    cnt_elems = len(ans[i])
    if nokori_b >= len(ans[i]) - 1:
        ans[i].sort(reverse=True)
        nokori_b -= (len(ans[i]) - 1)
    else:
        ans[i] = sorted(ans[i][:nokori_b + 1], reverse=True) + ans[i][nokori_b + 1:]
        break

res = []
for li in ans:
    for num in li:
        res.append(num)
print(*res)
