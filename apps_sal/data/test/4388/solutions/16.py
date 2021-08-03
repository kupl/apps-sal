n = str(input())
ans = ''
for i in range(3):
    if n[i] == '9':
        ans += '1'
    else:
        ans += '9'
print(ans)
