a = input()
l = input().split()
yes = 0
for i in l:
    if i[0] == a[0] or i[1] == a[1]:
        yes = 1
        break
if yes:
    print('YES')
else:
    print('NO')
