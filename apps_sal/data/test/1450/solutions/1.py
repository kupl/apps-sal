s = input()
ans = []
cnt1 = 0
for c in s:
    if c == '1':
        cnt1 += 1
    else:
        ans += [c]
j = 0
while j < len(ans) and ans[j] == '0':
    j += 1
ans = ans[:j] + ['1'] * cnt1 + ans[j:]
print(''.join(ans))
