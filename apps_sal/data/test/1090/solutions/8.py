(str_len, cng_cnt) = input().split(' ')
str_input = list(input())
str_len = int(str_len)
cng_cnt = int(cng_cnt)
tmp1 = ''
cnt = 0
cnt2 = 0
for st in str_input:
    if tmp1 == st:
        cnt = cnt + 1
    else:
        cnt2 = cnt2 + 1
    tmp1 = st
if cng_cnt < cnt2 - 1:
    c_up = cng_cnt * 2
else:
    c_up = cnt2 * 2 + (cng_cnt - cnt2)
ans = cnt + c_up
if ans >= str_len:
    ans = str_len - 1
print(ans)
