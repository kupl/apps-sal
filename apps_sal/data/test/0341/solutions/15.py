import math

def main():
	N, K = [int(n) for n in input().split(" ")]
	R, S, P = [int(p) for p in input().split(" ")]
	T = list(input())
	T.reverse()
	cnt = 0
	for i in range(K):
		tmp = []
		for j in range(math.ceil((N - i) / K)):
			if len(tmp) == 0 or T[i + j * K] != tmp[-1][0]:
				if T[i + j * K] == "r":
					tmp.append(["r", P, 1])
				elif T[i + j * K] == "s":
					tmp.append(["s", R, 1])
				elif T[i + j * K] == "p":
					tmp.append(["p", S, 1])
			else:
				tmp[-1][2] += 1
		for l in range(len(tmp)):
			cnt += tmp[l][1] * math.ceil(tmp[l][2] / 2)

	print(cnt)


main()
