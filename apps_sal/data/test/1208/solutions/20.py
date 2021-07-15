n = int(input())
mas = [0] * n
dict = {}

for i in range(n):
	sign, r = input().split()
	r = int(r)
	if (i == 0):
		isMinus = sign == '-'		
	if sign == '+':
		dict[r] = i
	else:
		start = dict.get(r, 0)
		for j in range(start, i):
			mas[j] += 1
		dict.pop(r, None)
		
for i in dict.values():
	for j in range(i, n):
		mas[j] += 1

max = -1
mini = -1
for i in range(n):
	if mas[i] > max:
		max = mas[i]
		mini = i

if mini == 0 and isMinus:
	max += 1
print(max)
