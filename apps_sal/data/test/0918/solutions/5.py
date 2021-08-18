
import time

(n, m) = (int(i) for i in input().split())
a = {}

for i in range(m):
    a[i] = []

for i in range(n):
    (f, r, s) = (i for i in input().split())
    r = int(r) - 1
    a[r].append([f, int(s)])

start = time.time()
ans = []

for i in range(m):
    a[i] = sorted(a[i], key=lambda x: x[1], reverse=True)
    if (len(a[i]) > 2) and (a[i][1][1] == a[i][2][1]):
        ans.append('?')
    else:
        ans.append(a[i][0][0] + " " + a[i][1][0])

for i in range(m):
    print(ans[i])
finish = time.time()
