n = int(input())
p = []
for i in range(n):
    (x, y) = map(int, input().split())
    p.append([x - 1, y - 1])
ans = []
k = 0
i = 0
while 1:
    if p[i][0] in p[p[i][1]]:
        ans += [i, p[i][1]]
        i = p[i][0]
    else:
        ans += [i, p[i][0]]
        i = p[i][1]
    k += 2
    if k >= n:
        break
for i in range(n):
    print(ans[i] + 1, end=' ')
