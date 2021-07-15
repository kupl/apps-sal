n = int(input())
stripes = [int(x) for x in input().split()] + [-1]
ln = 1
while ln < n and stripes[ln] == stripes[ln - 1]:
    ln += 1
cur = ln
flag = True
for i in range(ln, n + 1):
    if stripes[i] != stripes[i - 1]:
        if cur != ln:
            flag = False
            break
        cur = 0
    cur += 1
if flag:
    print('YES')
else:
    print('NO')
