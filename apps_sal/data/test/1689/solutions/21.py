from sys import stdin as fin

n = int(fin.readline())
flag = False
out = []
for i in range(n):
    l, r = fin.readline().strip().split('|')
    if not flag and l == 'OO':
        flag = True
        l = '++'
    elif not flag and r == 'OO':
        flag = True
        r = '++'
    out.append(l + '|' + r)
if flag:
    print("YES")
    print('\n'.join(out))
else:
    print("NO")
