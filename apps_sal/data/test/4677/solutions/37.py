s = str(input())
ans = ''
for i in range(len(s)):
    if s[i] != 'B':
        ans += s[i]
    elif ans != '':
        ans = ans[:-1]
print(ans)
