

n = int(input())
a = list(map(int,input().split(" ")))
m = int(input())
b = list(map(int,input().split(" ")))

i,j = 0,0
res = 0
x,y = 0,0
last_i,last_j = -1,-1
while(i < n and j < m):
	# print(i,j,x,y)
	if(last_i != i):
		x += a[i]
	if(last_j != j):
			y += b[j]
	last_i,last_j = i,j
	if(x == y):
		i += 1
		j += 1
		res += 1
		x = 0
		y = 0
	if(x<y):
		i += 1
	if(x>y):
		j += 1

if(i == n and j == m):
	print(res)
else:
	print("-1")
