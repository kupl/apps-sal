string = input()
r_cnt = 0
l_cnt = 0
flg = False
ans = [0 for _ in range(len(string))]
for i, s in enumerate(string):
    if s == "R":
        if flg:
            ans[pos - 1] += l_cnt // 2
            ans[pos] += (l_cnt + 1) // 2
            l_cnt = 0
            flg = False
        r_cnt += 1
    else:
        if not flg:
            pos = i
            ans[i - 1] += (r_cnt + 1) // 2
            ans[i] += r_cnt // 2
            r_cnt = 0
            flg = True
        l_cnt += 1
ans[pos - 1] += l_cnt // 2
ans[pos] += (l_cnt + 1) // 2

print(*ans)
