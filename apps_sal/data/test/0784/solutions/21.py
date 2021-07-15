from math import *
a ,b = map(int, input().split())
ans = [b]
per = 0
while b > a:
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
        ans.append(b)
    elif b % 2 == 0:
        b = b // 2
        ans.append(b)
    else:
        per = 1
        break
if per == 0 and b == a:
    print('YES')
    print(len(ans))
    ans.reverse()
    print(' '.join(map(str, ans)))
else:
    print('NO')
