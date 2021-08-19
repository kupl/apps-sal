(n, k) = input().split()
n = int(n)
k = int(k)
l = input()
d = {}
for val in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    d[val] = 0
for val in l:
    d[val] += 1
opened = {}
flag = 0
for val in l:
    if val not in opened:
        opened[val] = 1
    d[val] -= 1
    if len(opened) > k:
        flag = 1
        break
    if d[val] == 0:
        del opened[val]
if flag == 0:
    print('NO')
else:
    print('YES')
