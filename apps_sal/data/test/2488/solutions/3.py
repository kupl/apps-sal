n,d,a=list(map(int,input().split()))

xh=[list(map(int, input().split())) for _ in range(n)]
xh.sort()

cnt=0

import heapq  # heapqライブラリのimport
#heapq.heapify(a)  # リストを優先度付きキューへ
#heapq.heappop(a)  # 最小値の取り出し
#heapq.heappush(a, -2)

bomb=0
he=[]
heapq.heapify(he)
dic={}

for i in range(n):
    #print(xh[i],bomb,he)
    (x,h)=xh[i]

    if bomb==0:
        secchi=x+d
        count=((-1*h)//a)*(-1)
        damage=count*a
        cnt+=count
        dic[secchi]=damage
        bomb+=damage
        heapq.heappush(he, secchi)
    else:
        while a:
            tmp=heapq.heappop(he)  
            if tmp+d<x:
                bomb-=dic[tmp]
            else:
                heapq.heappush(he, tmp)
                break
            if bomb==0:
                break

        if bomb<h:
            h-=bomb
            secchi=x+d
            count=((-1*h)//a)*(-1)
            damage=count*a
            cnt+=count
            dic[secchi]=damage
            bomb+=damage
            heapq.heappush(he, secchi)



print(cnt)


