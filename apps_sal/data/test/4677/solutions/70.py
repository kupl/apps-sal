i = input()
ans = ''
for s in i:
    if s != 'B':
        ans += s
    else:
        ans = ans[:-1]
print(ans)
