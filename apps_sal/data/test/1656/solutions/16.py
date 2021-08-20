s = input()
wtot = 0
for i in range(1, len(s)):
    if s[i] == 'v' and s[i - 1] == 'v':
        wtot += 1
wleft = 0
ans = 0
for i in range(len(s)):
    if i > 0 and s[i] == 'v' and (s[i - 1] == 'v'):
        wleft += 1
    elif s[i] == 'o':
        ans += wleft * (wtot - wleft)
print(ans)
