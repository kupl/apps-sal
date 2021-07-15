from collections import deque
n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a = list(map(int, input().split()))
    g[a[0]-1].append(a[1]-1)
    g[a[1]-1].append(a[0]-1)
l = [True] * n
ans = [0] * n
x = deque([1])
while len(x) > 0:
    a = x.popleft()
    for i in g[a-1]:
        if l[i]:
            x.append(i+1)
            ans[i] = a
            l[i] = False
if l.count(True) == 0:
    print("Yes")
    for i in range(1, n):
        print(ans[i])
else:
    print("No")
