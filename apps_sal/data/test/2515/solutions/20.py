import math

def main():
	prime = [2, 3, 5, 7]
	for n in range(11, 100001):
		for p in prime:
			if n % p == 0:
				break
			if p > math.sqrt(n):
				prime.append(n)
				break
	sim = []
	j = 0
	for i in range(1, len(prime)):
		p = prime[i]
		q = int((p + 1) / 2)
		while q > prime[j]:
			j += 1
		else:
			if q == prime[j]:
				sim.append(p)
	sim.append(12345678)

	sim_n = [0]
	k = 0
	for s in range(1, 100001):
		if s == sim[k]:
			sim_n.append(sim_n[-1] + 1)
			k += 1
		else:
			sim_n.append(sim_n[-1])

	Q = int(input())
	for i in range(Q):
		l, r = [int(a) for a in input().split(" ")]
		print(sim_n[r] - sim_n[l - 1])

main()
