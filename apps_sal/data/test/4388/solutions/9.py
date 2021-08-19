s = input()
ans = ''
for w in s:
    if w == '1':
        ans += '9'
    else:
        ans += '1'
ans = int(ans)
print(ans)
