# 5 chel och
# pervii so vtorim etc, esli nechet lst stoit

radost = []
for i in range(5):
    radost.append(list(map(int, input().split())))

mr = 0

def cr(m):
    nonlocal radost
    return  radost[m[0]][m[1]] + \
            radost[m[1]][m[0]] + \
            radost[m[1]][m[2]] + \
            radost[m[2]][m[1]] + \
           (radost[m[2]][m[3]] + \
            radost[m[3]][m[2]]) * 2 + \
           (radost[m[3]][m[4]] + \
            radost[m[4]][m[3]]) * 2

for a in range(5):
    for b in range(5):
        for c in range(5):
            for d in range(5):
                for e in range(5):
                    m = [a, b, c, d, e]
                    if len(set(m))==5:
                        mr = max(mr, cr(m))

print(mr)

