for T in range(int(input())):
	n, k = list(map(int, input().split()))
	s = input()
	lp = 0
	rp = 0
	l = []
	for i in range(k * 2 - 2):
		while lp < n and s[lp] != '(' or lp < i:
			lp += 1
		while rp < n and s[rp] != ')' or rp < i:
			rp += 1
		if i % 2 == 0 and s[i] == '(' or i % 2 == 1 and s[i] == ')':
			continue
		elif i % 2 == 0:
			lp += 1
			s = s[: i] + s[i: lp][::-1] + s[lp:]
			l.append([i + 1, lp])
			rp = i

		else:
			rp += 1
			s = s[: i] + s[i: rp][::-1] + s[rp: ]
			l.append([i + 1, rp])
			lp = i
	
	for i in range(k * 2 - 2, (n+k+k-2)//2):
		while lp < n and s[lp] != '(' or lp < i:
			lp += 1
		while rp < n and s[rp] != ')' or rp < i:
			rp += 1
		if i<(n+k+k-2)//2 and s[i] == '(' or i>=(n+k+k-2)//2 and s[i] == ')':
			continue
		elif i<(n+k+k)//2:
			lp += 1
			s = s[: i] + s[i: lp][::-1] + s[lp: ]
			l.append([i + 1, lp])
			rp = i

		else:
			rp += 1
			s = s[: i] + s[i: rp][::-1] + s[rp: ]
			l.append([i + 1, rp])
			lp = i
	print(len(l))
	for i in l:
		print(*i)

