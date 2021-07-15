r,c,n,k = list(map(int,input().split()))
xy = [list(map(int,input().split())) for i in range(n)]
field = [[0]*c for i in range(r)]
for i in range(n):
    field[xy[i][0]-1][xy[i][1]-1] = 1
num = 0
for i in range(r):
    for j in range(c):
        for i2 in range(i,r):
            for j2 in range(j,c):
                num2 = 0
                for i3 in range(i,i2+1):
                    for j3 in range(j,j2+1):
                        if field[i3][j3] == 1:
                            num2 += 1
                if num2 >= k:
                    num += 1
print(num)

