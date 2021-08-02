from collections import deque
from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, m = nii()

tree = [[] for i in range(n)]
for i in range(m):
    a, b = nii()
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

ans = [-1 for i in range(n)]
ans[0] = 1

que = deque()
que.append(0)

while que:
    x = que.popleft()
    for i in tree[x]:
        if ans[i] == -1:
            ans[i] = x
            que.append(i)

if -1 in ans:
    print('No')
else:
    print('Yes')
    for i in ans[1:]:
        print(i + 1)
