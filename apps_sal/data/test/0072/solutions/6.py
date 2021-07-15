from collections import Counter

def solve(n, ribbons):
	L = len(ribbons[0])
	a = [Counter(r).most_common(1)[0][1] for r in ribbons]

	r = sorted([(x, i) for i, x in enumerate(a)], reverse=True)

	if n == 1:
		c = Counter(a)
		if c[L - 1] == 1:
			for i in range(3):
				if a[i] == L - 1: return i
		if c[L - 1] > 1:
			return 3
		if c[L] + c[L - 2] == 1:
			for i in range(3):
				if a[i] == L or a[i] == L-2:
					return i
		if c[L] + c[L - 2] > 1:
			return 3

	if r[1][0] == r[0][0]:
		return 3
	if r[1][0] + n >= L:
		return 3
	return r[0][1]

	print(a)

def main():
	n = int(input())
	cats = ('Kuro', 'Shiro', 'Katie', 'Draw')

	ribbons = [input().strip() for _ in range(3)]

	# print(ribbons)
	k = solve(n, ribbons)
	print(cats[k])

def __starting_point():
	main()
__starting_point()
