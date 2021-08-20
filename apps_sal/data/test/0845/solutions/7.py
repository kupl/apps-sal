a = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
r = [' qwertyuiop', ' asdfghjkl;', ' zxcvbnm,./']
l = ['wertyuiop', 'sdfghjkl;', 'xcvbnm,./']
s = input().strip()
str = input().strip()
ans = []
if s == 'L':
    for i in str:
        for j in range(3):
            if i in a[j]:
                ans.append(l[j][a[j].find(i)])
                break
else:
    for i in str:
        for j in range(3):
            if i in a[j]:
                ans.append(r[j][a[j].find(i)])
                break
print(''.join(ans))
