n, m = map(int, input().split())
l1 = [list(map(int, input().split())) for i in range(n)]
l2 = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        l1[i][j], l2[i][j] = min(l1[i][j], l2[i][j]), max(l1[i][j], l2[i][j])
ans = True
for i in range(1, n):
    for j in range(m):
        if l1[i][j] <= l1[i - 1][j] or l2[i][j] <= l2[i - 1][j]:
            ans = False
for i in range(n):
    for j in range(1, m):
        if l1[i][j] <= l1[i][j - 1] or l2[i][j] <= l2[i][j - 1]:
            ans = False
if ans:
    print('Possible')
else:
    print('Impossible')
