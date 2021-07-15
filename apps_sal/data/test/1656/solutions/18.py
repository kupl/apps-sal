s = input()
s = s.strip('o')
v = []
o = []

cnt_v = 0
cnt_o = 0
for i in range(len(s)):
    if s[i] == 'v':
        if cnt_o:
            o.append(cnt_o)
            cnt_o = 0
        cnt_v += 1
    else:
        if cnt_v:
            v.append(cnt_v)
            cnt_v = 0
        cnt_o += 1

v.append(cnt_v)

left = v[0]
left_cnt = 1
ans = 0
all_v = sum(v)
len_v = len(v)

for i in range(len(o)):
    ans += (left - left_cnt) * o[i] * (all_v - left - len_v + left_cnt)
    left += v[i + 1]
    left_cnt += 1

print(ans)

