from collections import deque

n = int(input())
arr = [int(i) for i in input()]
ans = [0 for i in range(n)]

indx = [[] for i in range(3)]

for i in range(n):
	indx[arr[i]].append(i)


for i in range(3):
	indx[i] = deque(indx[i])

x = n//3


if len(indx[2])>x:
	diff = len(indx[2])-x
	while diff>0:
		if(len(indx[0]) < x):
			indx[0].append(indx[2][0])
			indx[2].popleft()
		elif len(indx[1]) < x:
			indx[0].append(indx[2][0])
			indx[2].popleft()
		diff-=1

if len(indx[1])>x:
	diff = len(indx[1])-x
	while diff!=0:
		if(len(indx[0]) < x):
			indx[0].append(indx[1][0])
			indx[1].popleft()
		elif len(indx[2]) < x:
			indx[2].append(indx[1][-1])
			indx[1].pop()
		diff-=1


if len(indx[0])>x:
	diff = len(indx[0])-x
	while diff!=0:
		if(len(indx[2]) < x):
			indx[2].append(indx[0][-1])
			indx[0].pop()
		elif len(indx[1]) < x:
			indx[1].append(indx[0][-1])
			indx[0].pop()
		diff-=1

for i in range(3):
	for j in indx[i]:
		ans[j] = i

print(''.join(str(i) for i in ans))

