def main():
	import math
	N = int(input())
	n = math.ceil(math.log(100000000000, 4)) # toriaezu BIG ENOUGH na number
	M = int('10' * n, 2)
	B = format(N + M, 'b')
	print(even_toggle(B))

def even_toggle(b):
	r = []
	for i in range(len(b)):
		if i % 2 == 0:
			r.insert(0, b[-i-1])
		else:
			r.insert(0, str(1 - int(b[-i-1])))
	head_zeroes = 0
	for i in range(len(r)):
		if r[i] == "0":
			head_zeroes += 1
		else:
			break
	return "".join(r[head_zeroes:]) or "0"

main()
