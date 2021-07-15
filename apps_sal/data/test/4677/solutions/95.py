s = input()
ans = ''

for c in s:
    if c != 'B':
        ans += c
    else:
        ans = ans[:-1]

print(ans)
