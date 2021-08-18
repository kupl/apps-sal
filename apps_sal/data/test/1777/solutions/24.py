n = int(input())
a = [input() for i in range(n)]
kk = {}
for i in a:
    if i[0] == ')' and i[-1] == '(':
        continue
    cnt = 0
    flag1 = False
    flag2 = False
    isFirst = False
    for j in i:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt > 0:
            flag1 = True
            if not flag2:
                isFirst = True
        if cnt < 0:
            flag2 = True
    flag = False
    if cnt == 0:
        if flag2:
            continue
        else:
            flag = True
    if cnt > 0:
        if flag2:
            continue
        else:
            flag = True
    if cnt < 0:
        cnt_zakr = 0
        for j in i[::-1]:
            if j == '(':
                cnt_zakr -= 1
                if cnt_zakr < 0:
                    break
            else:
                cnt_zakr += 1
        else:
            flag = True
    if not flag:
        continue
    kk[cnt] = kk.get(cnt, 0) + 1
ans = 0
for i in kk.keys():
    if i >= 0:
        continue
    a = kk[i]
    b = kk.get(-i, 0)
    ans += min(a, b)
ans += kk.get(0, 0) // 2
print(ans)
