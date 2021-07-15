# -*- coding: utf-8 -*-

def getH(x, cx, y, cy, h):
    return h + abs(x-cx) + abs(y-cy)

N = int(input())
conditions = []
for i in range(N):
    x,y,h = map(int, input().split())
    if h > 0:
        conditions.append([x,y,h])

num_cnd = len(conditions)
if num_cnd==1:
    print(conditions[0][0],conditions[0][1],conditions[0][2])
    return

for cx in range(101):
    for cy in range(101):
        cnt = 0
        h = 0
        for i,cnd in enumerate(conditions):
            h_tmp = getH(cnd[0], cx, cnd[1], cy, cnd[2])
            if h_tmp >= 1:
                if i==0:
                    h = h_tmp
                    cnt += 1
                elif h == h_tmp:
                    cnt += 1
                    if cnt == num_cnd:
                        print(cx,cy,h)
                        return
                else:
                    break
            else:
                break
        

print('No')
