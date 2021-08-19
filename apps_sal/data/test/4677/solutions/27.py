S = input()
ans = ''
for s in S:
    if s == 'B':
        if ans:
            ans = ans[:-1]
    else:
        ans += s
print(ans)
