3

def dist(str1, str2):
	k = 0
	for i in range(6):
		if str1[i] != str2[i]:
			k += 1

	return k

def solve(promos):
	n = len(promos)

	dist_list = [0,0,0,1,1,2,2]
	min_k = 6

	for i in range(n):
		for j in range(i+1, n):
			d = dist(promos[i], promos[j])

			k = dist_list[d]
			if k < min_k: min_k = k
			if k == 0: break

	return min_k


def test():
	import random
	import string
	import time

	while True:
		n = 1000
		promos = []
		for i in range(n):
			promo = ''.join([random.choice(string.digits) for i in range(6)])
			promos.append(promo)

		if len(set(promos)) == n:
			break

	start = time.clock()
	k = solve(promos)
	print(k)
	end = time.clock()

	print('Time: {} sec'.format(end-start))


def main():
	n = int(input())
	promos = [None]*n
	for i in range(n):
		promos[i] = input()

	k = solve(promos)

	print(k)


def __starting_point():
	# test()
	main()

__starting_point()
