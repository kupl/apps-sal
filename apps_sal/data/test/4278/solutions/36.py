n = int(input())
s = [list(input()) for i in range(n)]
cnt_dic = {}
sum_cnt = 0

for i in range(n):
    s[i].sort()
    if str(s[i]) in cnt_dic:
        cnt_dic[str(s[i])] = cnt_dic[str(s[i])] + 1
    else:
        cnt_dic[str(s[i])] = 1

for n in cnt_dic.values():
    sum_cnt += int(n * (n - 1) / 2)

print(sum_cnt)
