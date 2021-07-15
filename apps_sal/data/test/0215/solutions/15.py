n = int(input())
s = str(input())

res = [[]]

for i in s:
	if ord(i) >= ord('A') and (ord(i)) <= ord('Z'):
		res.append([])
	else:
		res[-1].append(i)

mx = 0

for i in res:
	mx = max(mx, len(set(i)))

print(mx)
