n = int(input())
ans, cnt = 1, 0
for i in range(1, n + 1):
    j = i
    t_cnt = 0
    if i % 2 == 0:
        # print(i)
        while i % 2 == 0:
            i = i // 2
            t_cnt += 1
            # print(i, t_cnt)
        if t_cnt >= cnt:
            ans = j
            cnt = t_cnt

print(ans)
