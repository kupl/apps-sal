n,m = list(map(int,input().split()))
l = []
for i in range(1 << n):
    tmp = str(bin(i))[2:]
    l.append(tmp.zfill(n))
K = [list(map(int,input().split())) for _ in range(m)]
P = list(map(int,input().split()))
#print(P)
ans = 0
#print("----")
for i in range(len(l)):
    #スイッチの状態l[i]
    #付いている電球のリストO
    O = []
    for j in range(m):
        #電球のきになるすいっちの数K[j][0]
        ON = 0
        for ii in range(K[j][0]): #スイッチのリスト
            if l[i][K[j][ii+1] - 1] == "1":
                ON += 1
        if ON % 2 == P[j]:
            O.append(1)
        else:
            O.append(0)
    if sum(O) == m:
        #print(l[i])
        ans += 1
print(ans)


