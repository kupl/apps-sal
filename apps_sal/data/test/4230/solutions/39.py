#C問題

#ループ処理をスキップするコード→break,continue,return(関数方式)
x, n = map(int, input().split())
P = list(map(int, input().split()))
xm = x 
xM = x

for i in range(0,100):
    if n == 0:
        print(x)
        break
    xm = x - i
    xM = x + i
    mcounter = 0
    Mcounter = 0
    for j in range(len(P)):
        if xm == P[j]:
            mcounter += 1000
        if xM == P[j]:
            Mcounter += 1000
    if mcounter < 1000:
        print(xm)
        break
    if Mcounter < 1000:
        print(xM)
        break
