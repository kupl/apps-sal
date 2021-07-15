from sys import stdin, stdout

def solve(c, n):
	s_res = 0
	d_res = 0
	turn = 's'
	while len(c) > 0:
		left_is_max = c[0] > c[-1]
		max_card = c.pop(0 if left_is_max else -1)
		if turn == 's':
			s_res += max_card
			turn = 'd'
		else:
			d_res += max_card
			turn = 's'
	return (s_res, d_res)

def __starting_point():
	n_s = stdin.readline()
	cards_s = stdin.readline().split(' ')
	n = int(n_s)
	cards = [int(c) for c in cards_s]
	result = solve(cards, n)
	print(result[0], result [1])
__starting_point()
