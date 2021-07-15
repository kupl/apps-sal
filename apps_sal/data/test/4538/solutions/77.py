import math
N,D=(int(x) for x in input().split())
# 2次元配列
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)

count=0

for i in range(0,N):
	if math.sqrt(grid[i][0]**2 + grid[i][1]**2) <= D :
		count+=1

print(count)
