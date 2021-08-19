import math
(d, g) = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(d)]
sn = 1000
for i in range(2 ** d):
    ts = [False] * d
    score = 0
    tmp_sn = 0
    flg = True
    for j in range(d):
        if i >> j & 1:
            ts[j] = True
            score += data[j][0] * 100 * (j + 1) + data[j][1]
            tmp_sn += data[j][0]
    if score < g:
        for k in reversed(list(range(len(ts)))):
            if ts[k] == False:
                need = g - score
                s1 = (k + 1) * 100
                nnum = math.ceil(need / s1)
                if nnum < data[k][0]:
                    tmp_sn += nnum
                    break
                else:
                    flg = False
                    break
    if flg == True and sn > tmp_sn:
        sn = tmp_sn
print(sn)
