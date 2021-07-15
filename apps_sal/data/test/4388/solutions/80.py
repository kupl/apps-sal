n = str(input())
ans = ''
for i in range(3):
    if n[i] == '1':
        ans += '9'
    elif n [i] == '9':
        ans += '1'
print(int(ans))
