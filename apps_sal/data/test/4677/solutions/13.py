s = input()
ans = ''
for c in s:
    if c == '0':
        ans += c
    elif c == '1':
        ans += c
    elif ans != '':
        ans = ans[:-1]
print(ans)
