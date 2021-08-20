from collections import deque
(n, m) = list(map(int, input().split()))
r = [[] for i in range(n + 1)]
R = [[] for i in range(n + 1)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    r[a].append(b)
    r[b].append(a)
    R[a].append(b)
    R[b].append(a)
dep = [-1] * (n + 1)
dep[0] = 0
dep[1] = 0
data = deque([1])
d = 0
while len(data) > 0:
    p = data.popleft()
    for i in r[p]:
        if dep[i] == -1:
            dep[i] = dep[p] + 1
            data.append(i)
    r[p] = []
if not all((dep[i + 1] >= 0 for i in range(n))):
    print('No')
else:
    print('Yes')
    for i in range(2, n + 1):
        for j in R[i]:
            if dep[j] == dep[i] - 1:
                print(j)
                break
