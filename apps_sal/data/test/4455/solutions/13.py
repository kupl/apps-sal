n,k = [int(s) for s in input().split()]
r = [int(s) for s in input().split()]
q = [0]*n
for i in range(k):
    x,y = [int(s)-1 for s in input().split()]
    if r[x] > r[y]:
        q[x] += 1
    if r[y] > r[x]:
        q[y] += 1
r1 = []
for i in range(n):
    r1.append((r[i], i))
r1.sort()
lower = 0
ans = [0]*n
for i in range(n):
    if i > 0 and r1[i][0] > r1[i-1][0]:
        lower = i
    ans[r1[i][1]] = lower-q[r1[i][1]]

print(*ans, sep=" ")
