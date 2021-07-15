import sys, math
n = int(input())
ans = []
flag = 0
for i in range(n):
    z = input()
    if not flag:
        if z[0] == 'O' and z[1] == 'O':
            z = '++' + z[2:]
            flag = 1
        elif z[3] == 'O' and z[4] == 'O':
            z = z[:3] + '++'
            flag = 1
    ans.append(z)
if not flag:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(ans[i])
            

