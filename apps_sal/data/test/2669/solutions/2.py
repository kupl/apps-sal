n= int(input())
start= list(map(int,input().split()))
finish= list(map(int,input().split()))

task=[0]
act=0
for i in range(1,n):
	if start[i]>=finish[act]:
		task.append(i)
		act=i

for i in task:
	print(i,end=" ")


