s = input()
ans = ''
for char in s:
    if char == 'B':
        if ans == '':
            pass
        else:
            l = len(ans)
            ans = ans[0:l - 1]
    else:
        ans += char
print(ans)
