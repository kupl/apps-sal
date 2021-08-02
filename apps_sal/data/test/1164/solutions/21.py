from decimal import Decimal
check = input()
check = check + 'a'
bukvi = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
flag = 0
number = []
numbers = []
for symvol in check:
    if flag == 0:
        if symvol not in bukvi:
            flag = 1
    if flag == 1:
        if symvol not in bukvi:
            number += symvol
        else:
            numbers += [number]
            number = []
            flag = 0
ans = 0
for num in numbers:
    integ = []
    for i in range(len(num)):
        if num[i] != '.':
            integ += num[i]
        else:
            if i == len(num) - 3:
                integ += [num[i]]
    ans += Decimal(''.join(integ))
ans = str(ans)
if len(ans) > 3 and ans[-1] == ans[-2] == '0' and ans[-3] == '.':
    ans = ans[:-3]
res = []
cnt = 0
if len(ans) > 3 and ans[-3] == '.':
    for i in range(len(ans) - 4, -1, -1):
        if cnt == 3:
            res += ['.']
            cnt = 0
        res += ans[i]
        cnt += 1
    res.reverse()
    res += ans[-3:]
else:
    for i in range(len(ans) - 1, -1, -1):
        if cnt == 3:
            res += ['.']
            cnt = 0
        res += ans[i]
        cnt += 1
    res.reverse()
print(''.join(res))
