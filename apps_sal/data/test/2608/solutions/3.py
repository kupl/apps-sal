def color(x, y):
	# print(f'color(x = {x}, y = {y}) called')
	return 'white' if (x + y) % 2 == 0 else 'black'


def white(x1, y1, x2, y2):
	""" x1 <= x2, y1 <= y2 """
	# print(f'white(x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}) called')
	if x1 > x2 or y1 > y2:
		return 0

	if color(x1, y1) != color(x2, y2):
		return (x2 - x1 + 1) * (y2 - y1 + 1) // 2
	else:
		if color(x1, y1) == color(x1, y2) == color(x2, y1) == 'white':
			return ((x2 - x1 + 1) * (y2 - y1 + 1) + 1) // 2
		elif color(x1, y1) == color(x1, y2) == color(x2, y1) == 'black':
			return ((x2 - x1 + 1) * (y2 - y1 + 1) - 1) // 2
		else:
			return (x2 - x1 + 1) * (y2 - y1 + 1) // 2	


def black(x1, y1, x2, y2):
	""" x1 <= x2, y1 <= y2 """
	if x1 > x2 or y1 > y2:
		return 0

	return (x2 - x1 + 1) * (y2 - y1 + 1) - white(x1, y1, x2, y2)


def intersect_1D(x1, x2, x3, x4):
	""" x1 <= x2, x3 <= x4 """
	return max(x1, x3), min(x2, x4)


def intersect_2D(x1, y1, x2, y2, x3, y3, x4, y4):
	""" x1 <= x2, x3 <= x4, y1 <= y2, y3 <= y4 """
	xl, xr = intersect_1D(x1, x2, x3, x4)
	yl, yr = intersect_1D(y1, y2, y3, y4)
	return xl, yl, xr, yr


for i in range(int(input())):
	n, m = list(map(int, input().split()))
	# print(f'n = {n}, m = {m}')
	x1, y1, x2, y2 = list(map(int, input().split()))
	# print(f'x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}')
	x3, y3, x4, y4 = list(map(int, input().split()))
	# print(f'x3 = {x3}, y3 = {y3}, x4 = {x4}, y4 = {y4}')

	w0, b0 = white(1, 1, m, n), black(1, 1, m, n)
	# print(f'w0 = {w0}, b0 = {b0}')

	_b0 = black(x1, y1, x2, y2)
	# print(f'_b0 = {_b0}')
	w1, b1 = w0 + _b0, b0 - _b0

	_w1 = white(x3, y3, x4, y4)
	# print(f'_w1 = {_w1}')
	w2, b2 = w1 - _w1, b1 + _w1

	xl, yl, xr, yr = intersect_2D(x1, y1, x2, y2, x3, y3, x4, y4)
	# print(f'xl = {xl}, yl = {yl}, xr = {xr}, yr = {yr}')
	_b2 = black(xl, yl, xr, yr)
	# print(f'_b2 = {_b2}')
	w3, b3 = w2 - _b2, b2 + _b2

	print(w3, b3)

