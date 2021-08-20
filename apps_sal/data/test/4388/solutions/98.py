S = input()
ans = ''
for s in S:
    if s == '1':
        ans += '9'
    if s == '9':
        ans += '1'
print(ans)
