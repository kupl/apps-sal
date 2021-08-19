s = input()
arr = input().split()
p = False
for i in arr:
    if i[0] in s or i[1] in s:
        p = True
if p:
    print('YES')
else:
    print('NO')
