from sys import stdin
(n, m) = [int(i) for i in stdin.readline().split()]
ori = [int(i) for i in stdin.readline().split()]
pre = [-1] * n
ans = list()
for i in range(n - 1):
    if ori[i] != ori[i + 1]:
        pre[i + 1] = i
    else:
        pre[i + 1] = pre[i]
for i in range(m):
    (l, r, x) = [int(i) for i in stdin.readline().split()]
    tem = r - 1
    if ori[tem] != x:
        ans.append(str(r))
    elif pre[r - 1] == pre[l - 1]:
        ans.append('-1')
        continue
    else:
        ans.append(str(pre[r - 1] + 1))
print('\n'.join(ans))
