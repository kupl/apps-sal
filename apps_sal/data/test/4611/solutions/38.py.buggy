n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

pT, pX, pY = 0, 0, 0

for i in range(n):
    cT, cX, cY = d[i]
    mvT, mvX, mvY = abs(cT - pT), abs(cX - pX), abs(cY - pY)

    dam = mvT - (mvX + mvY)

    if dam % 2 == 1 or dam < 0:
        print('No')
        return

    pT, pX, pY = d[i]

print('Yes')
