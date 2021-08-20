from sys import *


def input():
    return stdin.readline()


(n, m) = map(int, input().split())
a = list(map(int, input().split()))
ans = []
difPre = [-1 for i in range(n)]
for i in range(1, n):
    if a[i] == a[i - 1]:
        difPre[i] = difPre[i - 1]
    else:
        difPre[i] = i - 1
for i in range(m):
    (l, r, x) = map(int, input().split())
    if a[r - 1] != x:
        ans.append(str(r))
    elif difPre[r - 1] >= l - 1:
        ans.append(str(difPre[r - 1] + 1))
    else:
        ans.append('-1')
print('\n'.join(ans))
