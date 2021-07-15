
for i in range(int(input())):
	s = input()
	lm, rm, um, dm = 0, 0, 0, 0
	xp, yp = 0, 0
	for ch in s:
		if ch == 'W':
			yp += 1
		elif ch == 'A':
			xp -= 1
		elif ch == 'S':
			yp -= 1
		else:
			xp += 1
		lm = min(lm, xp)
		rm = max(rm, xp)
		um = max(um, yp)
		dm = min(dm, yp)
	xp, yp = 0, 0
	lmfSet, rmfSet, umfSet, dmfSet = 0, 0, 0, 0
	if lm == 0:
		lml = 0
		lmf = 0
		lmfSet = 1
	if rm == 0:
		rml = 0
		rmf = 0
		rmfSet = 1
	if um == 0:
		uml = 0
		umf = 0
		umfSet = 1
	if dm == 0:
		dml = 0
		dmf = 0
		dmfSet = 1
	for i, ch in zip(list(range(1, len(s) + 1)), s):
		if ch == 'W':
			yp += 1
		elif ch == 'A':
			xp -= 1
		elif ch == 'S':
			yp -= 1
		else:
			xp += 1
		if xp == lm:
			lml = i
			if not lmfSet:
				lmf = i
				lmfSet = 1
		if xp == rm:
			rml = i
			if not rmfSet:
				rmf = i
				rmfSet = 1
		if yp == um:
			uml = i
			if not umfSet:
				umf = i
				umfSet = 1
		if yp == dm:
			dml = i
			if not dmfSet:
				dmf = i
				dmfSet = 1
	canx, cany = 0, 0
	if dml + 1 < umf or uml + 1 < dmf:
		cany = 1
	if lml + 1 < rmf or rml + 1 < lmf:
		canx = 1
	if canx:
		if cany:
			print(min((um - dm) * (rm - lm + 1), (um - dm + 1) * (rm - lm)))
		else:
			print((rm - lm) * (um - dm + 1))
	else:
		if cany:
			print((um - dm) * (rm - lm + 1))
		else:
			print((rm - lm + 1) * (um - dm + 1))



