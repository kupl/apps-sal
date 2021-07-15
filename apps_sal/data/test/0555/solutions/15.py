a = input()
ans = ''
for i in range(1, len(a)):
    if int(a[i]) >= 5:
        ans += str(9 - int(a[i]))
    else:
        ans += a[i]
if int(a[0]) >= 5:
    if a[0] != '9':
        ans = str(9 - int(a[0])) + ans
if int(a[0]) < 5 or int(a[0]) == 9:
    ans = a[0] + ans
print(ans)

