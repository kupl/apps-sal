n = int(input())
l = list(map(int,input().split()))
m = 0
for i in range(n):
	if l[i] >= 0:
		l[i] = -l[i] - 1
for i in range(n):
	if l[i] < 0 :
		m += 1
if m % 2 == 0:
	for i in range(n):
		print(l[i], end = " ")
else:
	maksi = -1000000000000
	for i in range(n):
		if abs(l[i]) > maksi:
			maksi = abs(l[i])
			mk = i
	l[mk] = -l[mk] - 1
	for i in range(n):
		print(l[i], end = " ")
