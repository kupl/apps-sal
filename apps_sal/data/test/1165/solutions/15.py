from sys import stdin

n, m = [int(i) for i in stdin.readline().split()]
a = [int(i) for i in stdin.readline().split()]
b = [None] * n
b[0] = -1
ans = [None] * m
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        b[i] = b[i - 1]
    else:
        b[i] = i - 1
for i in range(m):
    l, r, x = [int(j) for j in stdin.readline().split()]
    k = r - 1
    if a[k] != x:
        ans[i] = str(k + 1)
    elif b[k] + 1 >= l:
        ans[i] = str(b[k] + 1)
    else:
        ans[i] = ('-1')

print('\n'.join(ans))
