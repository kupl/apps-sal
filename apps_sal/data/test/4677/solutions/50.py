S = input()
ans = ''
for s in S:
    if s == '0':
        ans += '0'
    elif s == '1':
        ans += '1'
    elif len(ans) > 0:
        ans = ans[:-1]
print(ans)
