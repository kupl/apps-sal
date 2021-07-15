tmp = input().split(' ')
n = int(tmp[0])
m = int(tmp[1])
k = int(tmp[2])
tmp = input().split(' ')
pos = []
need = []
for i in range(k):
	pos.append(int(tmp[i]))
time = 0
for i in range(n):
	tmp = input().split(' ')
	need.clear()
	for j in range(m):
		need.append(int(tmp[j]))
	for j in range(m):
		curpos = pos.index(need[j])
		time = time + curpos + 1
		del pos[curpos]
		pos.insert(0,need[j])

print(time)

