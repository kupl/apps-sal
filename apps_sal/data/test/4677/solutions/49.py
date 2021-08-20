s = input()
ans = ''
for char in s:
    if char == '0':
        ans += '0'
    if char == '1':
        ans += '1'
    if char == 'B':
        ans = ans[:-1]
print(ans)
