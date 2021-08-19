t = input()
s = [i for i in input().split()]
good = False
for i in s:
    if i[0] == t[0]:
        good = True
    if i[1] == t[1]:
        good = True
if good:
    print('YES')
else:
    print('NO')
