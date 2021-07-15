T = int(input())

for _ in range(T):
	s = input()

	cleft=cup=cdown=cright=0
	left=up=down=right=0
	fleft=lleft=0
	fright=lright=0
	fup=lup=0
	fdown=ldown=0

	x=y=0
	for i, c in enumerate(s):
		if c=="W":
			y -= 1
			cup += 1
		elif c=="S":
			y += 1
			cdown += 1
		elif c=="A":
			x -= 1
			cleft += 1
		elif c=="D":
			x += 1
			cright += 1

		if x == left:
			lleft = i
		if x == right:
			lright = i
		if y == down:
			ldown = i
		if y == up:
			lup = i

		if x < left:
			left = x
			fleft=i
			lleft=i

		if x > right:
			right = x
			fright=i
			lright=i


		if y < up:
			up = y
			fup=i
			lup=i


		if y > down:
			down = y
			fdown=i
			ldown=i

	width = right - left + 1
	height = down - up + 1

	best = width * height

	if height > 2:
		if ldown < fup or lup < fdown:
			best = min(best, width * (height-1))
	if width > 2:
		if lleft < fright or lright < fleft:
			best = min(best, (width-1) * height)
	print(best)
