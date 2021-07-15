def main():
	K = int(input())
	rn = [0]
	r = [0] * K
	for i in range(K):
		ri = (rn[-1] * 10 + 7) % K
		if ri == 0:
			print(i + 1)
			return 0
		elif r[ri] == 0:
			r[ri] = 1
			rn.append(ri)
		elif r[ri] == 1:
			print(-1)
			return 0

main()
