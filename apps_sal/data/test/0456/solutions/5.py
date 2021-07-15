n = int(input())
a = input() + 'aaa'
ans = ''
i = 0
ogo = False
while i < n:
    if a[i:i + 3] == 'ogo':
        ans += '***'
        i += 3
        ogo = True
    elif a[i:i + 2] == 'go' and ogo:
        i += 2
    else:
        ogo = False
        ans += a[i]
        i += 1
print(ans)
