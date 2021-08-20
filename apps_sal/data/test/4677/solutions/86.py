s = input()
ans = ''
for i in range(len(s)):
    if s[i] != 'B':
        ans += s[i]
    else:
        ans = ans[:-1]
print(ans)
