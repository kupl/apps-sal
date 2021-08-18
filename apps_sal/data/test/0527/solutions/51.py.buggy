import collections
import math
s = input()
t = input()
# tを構成文字で、sにない文字があったらダメ。
# 構成できるなら最大でもlen(t)個しかないから、10^100の連結は必要ない

# 最も不足する文字を探す
ls = collections.Counter(s)
lt = collections.Counter(t)

time_dict = {}
tmp = 0
max_time = 0  # 一番少ないやつ
for t_key, t_val in list(lt.items()):
    if t_key not in ls:  # sの中にtの文字がない
        print((-1))
        return

# 多分TLEするかも。。
cnt = 0
tt = list(t[::-1])
idx = 0
ss = s
while tt != []:
    next_t = tt.pop()
    idx = ss.find(next_t)
    if idx == -1:
        cnt += len(ss)
        idx = s.find(next_t)
        ss = s[idx + 1:]
        cnt += idx + 1
    else:
        cnt += idx + 1
        ss = ss[idx + 1:]
print(cnt)
