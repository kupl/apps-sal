n = input()
ans = ''

for i in n:
    if i == '1':
        tmp = '9'
    elif i == '9':
        tmp = '1'
    else:
        tmp = i
    ans += tmp

print(ans)
