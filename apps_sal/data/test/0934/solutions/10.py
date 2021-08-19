t = input()
a = list(input().split())
can = False
for x in a:
    if x[1] == t[1]:
        can = True
    if x[0] == t[0]:
        can = True
if can:
    print('YES')
else:
    print('NO')
