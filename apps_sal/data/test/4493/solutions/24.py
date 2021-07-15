c=[list(map(int,input().split())) for _ in range(3)]
for i in range(2):
    if not (c[i+1][0]-c[i][0]==c[i+1][1]-c[i][1] and c[i+1][1]-c[i][1]==c[i+1][2]-c[i][2]):
        print("No")
        break
    if not (c[0][i+1]-c[0][i]==c[1][i+1]-c[1][i] and c[1][i+1]-c[1][i]==c[2][i+1]-c[2][i]):
        print("No")
        break
else:
    print("Yes")

