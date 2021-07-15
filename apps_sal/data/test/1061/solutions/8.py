import math
matrix=[[int(i) for i in input().split(" ")] for i in range(0,5)]
(x,y)=(0,0)
for i in range(0,5):
    for j in range(0,5):
        if matrix[i][j]==1:
            (x,y)=(i,j)
print(int(math.fabs(x-2)+math.fabs(y-2)))

