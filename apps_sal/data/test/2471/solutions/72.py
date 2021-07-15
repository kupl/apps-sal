H, W , N = list(map(int,input().split()))
from bisect import bisect_left
from bisect import bisect_right
matrix = []
for _ in range(N):
    x,y = list(map(int,input().split()))
    matrix.append([x-1,y-1])
ans = [0 for _ in range(10)]
cand = {}
for l in matrix:
    for x_r in [-2, -1 , 0]:
        for y_r in [-2, -1 , 0]:
            nowx = l[0] + x_r
            nowy = l[1] + y_r
            if nowx < 0 or nowy < 0 or nowx + 2>= H or nowy+ 2 >= W:
                continue
            #ここで起点(左上)nowx, nowy として　 9マスに着目する
            name = str(nowx) + ' '  +str(nowy)
            if name in cand : cand[name] += 1
            else: cand[name] = 1
tmp = ((H - 2) * (W - 2))
for x in list(cand.values()):
  ans[x] +=1
ans[0] =tmp - len(cand)
for x in ans:
    print(x)

