n = int(input())
cnt = 0
cur_cnt = 1
for i in range(n, 0, -1):
    cnt += min(cur_cnt, i)
    cur_cnt += 1
print(cnt)
