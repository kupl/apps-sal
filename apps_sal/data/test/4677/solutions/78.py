s = input()
ans = ''
for i in s:
    if i == 'B':
        if ans != '':
            ans = ans[:-1]
    else:
        ans += i
print(ans)
