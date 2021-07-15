import sys
input = sys.stdin.readline
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def main():
	N, A, B = getlist()
	if 1 + N < A + B or N > A * B:
		print(-1)
		return

	ans = [i for i in range(N, N - B, -1)]
	N2 = N - B; A2 = A - 1
	if A2 == 0:
		print(*ans)
		return
	p = N2 // A2
	q = N2 % A2
	B = [p] * A2
	B.append(0)
	for i in range(q):
		B[i] += 1
	# print(B)
	Bsum = [0] * A2
	for i in range(A2):
		Bsum[i] = Bsum[i - 1] + B[i]
	# print(Bsum)

	pre = []
	for i in range(A2):
		for j in range(B[i]):
			pre.append(Bsum[i] - j)
	# print(pre)
	answer = pre + ans
	print(*answer)




def __starting_point():
	main()
__starting_point()
