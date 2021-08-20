x = input()
deck = list(input().split())
get = False
for d in deck:
    if d[0] == x[0]:
        get = True
    if d[1] == x[1]:
        get = True
if get:
    print('YES')
else:
    print('NO')
