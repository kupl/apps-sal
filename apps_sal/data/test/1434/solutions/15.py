from collections import deque
n = int(input())
process = deque()
vs = []
for i in range(n):
	d, s = list(map(int, input().split()))
	if d == 1:
		process.append(i)
	vs.append((d, s))
edges = []
while process:
	a = process.popleft()
	d, s = vs[a]
	if d == 0:
		continue
	dd, ss = vs[s]
	vs[s] = (dd - 1, ss ^ a)
	if dd == 2:
		process.append(s)
	edges.append((a, s))
print(len(edges))
for a, b in edges:
	print(a, b)




# Made By Mostafa_Khaled

