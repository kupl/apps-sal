n = int(input())
x = list(map(int, input().split(" ")))
x.sort()
q = int(input())
m = list()

for i in range(q):
	m_i = int(input())
	m.append([i, m_i, 0])

m.sort(key = lambda x: x[1])
# print(m)

i = 0
j = 0
count = 0
while j < q:
	if i == n:
		m[j][2] = count
		j += 1
		continue

	if x[i] <= m[j][1]:
		count += 1
		i += 1
	else:
		m[j][2] = count
		j += 1


m.sort(key = lambda x: x[0])
# print(m)
for x in m:
	print(x[2])
