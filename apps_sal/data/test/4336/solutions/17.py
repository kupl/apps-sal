# C - Rectangle Cutting
W,H,x,y = map(int,input().split())
S = W*H

# H,W の中心と x,y の距離
distx = abs(W/2 - x)
disty = abs(H/2 - y)

if distx == disty == 0:
    ans = (S/2,1)
else:
    ans = (S/2,0)
print(*ans)
