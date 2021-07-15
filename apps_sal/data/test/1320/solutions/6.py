n =int(input())
x=[[i for i in input()] for j in range(0,n)]
summ =0
for i in range(n):
	cur = 0
	for j in range(n):
		if (x[i][j]=='C'):
			cur+=1
	summ+=cur*(cur-1)//2
for j in range(n):
	cur = 0
	for i in range(n):
		if (x[i][j]=='C'):
			cur+=1
	summ+=cur*(cur-1)//2
print(summ)
