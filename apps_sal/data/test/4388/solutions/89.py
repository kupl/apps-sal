n = list(input())
ans = ''

for w in n:
    if w == '1':
        ans += '9'
    else:
        ans += '1'

print(ans)
