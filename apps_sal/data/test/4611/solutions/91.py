N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

pT, pX, pY = 0, 0, 0

for i in range(N):
    cT, cX, cY = l[i]
    mvT, mvX, mvY = abs(cT-pT), abs(cX-pX), abs(cY-pY)
    
    dam = mvT - (mvX+mvY)

    if dam %2 == 1 or dam < 0:
        print('No')
        return

    pT, pX, pY = l[i]

print('Yes')


