s = input()
curnum = 0
ans = 0
dr = 0
n = len(s)
s += 'aaa'
i = 0
while i < n:
    if '0' <= s[i] <= '9':
        curnum = 10 * curnum + int(s[i])
    elif s[i] == '.':
        if '0' <= s[i + 1] <= '9' and '0' <= s[i + 2] <= '9' and (not '0' <= s[i + 3] <= '9'):
            dr += 10 * int(s[i + 1]) + int(s[i + 2])
            i = i + 2
    else:
        ans += curnum
        curnum = 0
    i += 1
ans += curnum
ans += dr // 100
ans2 = dr % 100
if ans2 == 0:
    ans2 = ''
elif ans2 < 10:
    ans2 = '.0' + str(ans2)
else:
    ans2 = '.' + str(ans2)
ans = int(ans)
ans = str(ans)
nans = ''
for i in range(len(ans)):
    if i % 3 == 0 and i != 0:
        nans += '.'
    nans += ans[len(ans) - 1 - i]
print(nans[::-1] + ans2)
