n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    ab[i].append(i)

ab_l = sorted(ab, key=lambda x: x[1])
ab_ll = sorted(ab_l, key=lambda x: x[0])

temp = 1
for j in range(m):
    if j==0 or ab_ll[j][0] != ab_ll[j-1][0]:
        temp = 1
    else:
        temp +=1
    ab_ll[j].append(temp)

ab_lll = sorted(ab_ll, key=lambda x: x[2])

for i in range(m):
    print(str(ab_lll[i][0]).zfill(6)+str(ab_lll[i][3]).zfill(6))
