W,H,N= list(map(int,input().split()))
Black = [[True for _ in range(W)] for i in range(H)]
for i in range(N):
    x,y,a = list(map(int,input().split()))
    for j in range(H):
        for k in range(W):
            if a == 1:
                if k < x:
                    Black[j][k] = False
            elif a == 2:
                if k >= x:
                    Black[j][k] = False
            elif a == 3:
                if j < y:
                    Black[j][k] = False
            elif a == 4:
                if j >= y:
                    Black[j][k] = False
                    #print(Black)

c = 0
#print(Black)
for i in range(H):
    c += Black[i].count(True)
print(c)




