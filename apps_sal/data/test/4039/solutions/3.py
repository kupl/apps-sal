n, r = [int(i) for i in input().split()]

proj = [[0 for i in range(2)] for j in range(n)]
posb = 0
sum_neg = 0

for i in range(n):
    proj[i][0], proj[i][1] = [int(j) for j in input().split()]
    if proj[i][1] >= 0:
        posb += 1
    else:
        sum_neg += proj[i][1]

negb = n - posb

proj = sorted(proj, key=lambda elem: elem[1])

proj_pos = sorted(proj[negb:], key=lambda elem: elem[0])

res = True

i = 0

while res and i < posb:
    if r < proj_pos[i][0]:
        res = False
    else:
        r += proj_pos[i][1]
        i += 1

if res:
    proj_neg = sorted(proj[:negb], key=lambda elem: elem[0] + elem[1], reverse=True)

    i = 0

    while res and i < negb and r >= 0:
        if r < proj_neg[i][0]:
            res = False
        else:
            r += proj_neg[i][1]
            i += 1

    if r >= 0 and res:
        print("YES")
    else:
        print("NO")


else:
    print("NO")
