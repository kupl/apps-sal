n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
max_cnt = 0
now_cnt = 0
for i in range(n):
    if len(set(l[i])) == 1:
        now_cnt += 1
        max_cnt = max(max_cnt, now_cnt)
    else:
        now_cnt = 0
print("Yes" if max_cnt >= 3 else "No")
