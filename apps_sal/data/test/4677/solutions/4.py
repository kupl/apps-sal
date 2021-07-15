s = input()

ans = ''
for i in range(len(s)):
    if s[i] == 'B':
        ans = ans[:-1]
    else:
        ans += s[i]

print(ans)
