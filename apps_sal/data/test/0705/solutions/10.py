def solution():
	n = int(input())
	x = [int(a) for a in input().split(' ')]
	dicx = {}
	for _x in x:
		dicx[_x] = True
	y = [int(a) for a in input().split(' ')]
	dicy = {}
	for _y in y:
		dicx[_y] = True

	ans = 0
	for _x in dicx:
		for _y in dicy:
			current = _x ^ _y
			if  current in dicx or current in dicx:
				ans += 1


	if ans%2 == 0:
		print('Karen')
	else:
		print('Koyomi')

solution()
