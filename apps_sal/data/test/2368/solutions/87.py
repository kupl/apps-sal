from collections import deque
(n, m) = map(int, input().split())
ans = [list(map(int, input().split())) for i in range(2)]
l = [[] for i in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    l[a - 1].append(b - 1)
    l[b - 1].append(a - 1)
boo = [-1] * n
flag = 0
for i in range(n):
    if boo[i] == -1:
        q = deque([])
        q.append(i)
        ma = 0
        wa = 0
        while q:
            a = q.popleft()
            if boo[a] == -1:
                boo[a] += 1
                ma += ans[0][a]
                wa += ans[1][a]
                for j in l[a]:
                    if boo[j] == -1:
                        q.append(j)
        if ma != wa:
            flag = 1
            break
if flag == 0:
    print('Yes')
else:
    print('No')
