N = list(range(8))
test = int (input())
for i_test in range(test):
    if (i_test): input()
    x1,y1,x2,y2=0,0,0,0
    map = [input() for i in N]
    for i in N:
        for j in N:
            if (map[i][j]=="K"): x1,y1,x2,y2 = x2,y2,i,j
    if (abs(x1-x2)%4==0 and abs(y1-y2)%4==0): print ("YES")
    else: print ("NO")

