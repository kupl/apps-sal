n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([i - a[i], i])
b.sort()
comp = []
now = [b[0][1]]
for i in range(1, n):
    if b[i - 1][0] == b[i][0]:
        now.append(b[i][1])
    else:
        comp.append(now)
        now = [b[i][1]]
comp.append(now)
ans = 0
for i in range(len(comp)):
    now = 0
    for elem in comp[i]:
        now += a[elem]
    ans = max(ans, now)
print(ans)
