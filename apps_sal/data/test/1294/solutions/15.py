n = int(input())
for i in range(n):
	st = input()
	st += '#'
	k = len(st)
	lastch = '.'
	lastl = 0
	able = [False for i in range(256)]
	for j in range(k):
		if st[j] != lastch:
			if lastl % 2 == 1:
				able[ord(lastch)] = True
			lastl = 1
			lastch = st[j]
		else:
			lastl += 1
	for j in range(ord('a'),ord('z')+1):
		if able[j]:
			print(chr(j),end='')
	print()
