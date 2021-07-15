def main():
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	A.sort()
	l = A[-1]
	p = [1] * l
	for i in range(len(A)):
		a = A[i]
		if p[a-1] == 1:
			p[a-1] = 2
			for j in range(2 * a - 1, l, a):
				p[j] = 0
		elif p[a-1] == 2:
			p[a-1] = 0
	print(len([x for x in A if p[x - 1] in [1, 2]]))

main()
