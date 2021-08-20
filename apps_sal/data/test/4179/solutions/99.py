(n, m, c) = map(int, input().split())
b = list(map(int, input().split()))
li = [list(map(int, input().split())) for i in range(n)]
cnt = 0
su = 0
for i in range(n):
    for j in range(m):
        su += li[i][j] * b[j]
    if su + c > 0:
        cnt += 1
    su = 0
print(cnt)
