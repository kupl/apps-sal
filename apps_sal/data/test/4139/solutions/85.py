import math
import itertools
import collections

def main():
	N = int(input())
	digit = math.floor(math.log10(N)) + 1
	if digit <= 2:
		print(0)
		return 0
	cnt = int(3 * (3 ** (digit - 1) - 2 ** (digit + 1) + 2 * digit + 1) / 2)

	num = ['3', '5', '7']
	cand = ["".join(list(x)) for x in itertools.product(num, repeat=digit)]
	for ca in cand:
		c = collections.Counter(ca)
		if c['3'] and c['5'] and c['7'] and int(ca) <= N:
			cnt += 1
	print(cnt)

main()
