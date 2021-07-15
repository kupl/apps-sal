n = int(input())
pr = 0
mn = [1]
prib = [0]
b = 1
for _ in range(n):
	s = input().split()
	if s[0] == 'add':
		prib[-1] += 1
	elif s[0] == 'for':
		mn.append(int(s[1]))
		prib.append(0)
	else:
		e = prib.pop() * mn.pop()
		prib[-1] += e
		if prib[-1] > 2**32-1:
			b = 0
			break
if b:
	if prib[0] <= 2**32-1:
		print(prib[0])
	else:
		print('OVERFLOW!!!')
else:
	print('OVERFLOW!!!')
