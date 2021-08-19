(n, m) = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(m)]
l = sorted(l, key=lambda x: (x[1], x[0]))
cnt = 0
con_l = 0
for i in range(m):
    if con_l <= l[i][0]:
        cnt += 1
        con_l = l[i][1]
print(cnt)
