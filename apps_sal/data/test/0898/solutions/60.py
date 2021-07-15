import math

def main():
	N, M = [int(a) for a in input().split(" ")]
	divM = []
	for i in range(1, int(math.sqrt(M)) + 1):
		if M % i == 0:
			divM += [i, M // i]
	divM.sort()
	divM = list(filter(lambda m: m >= N, divM))
	print(M // divM[0])

main()
