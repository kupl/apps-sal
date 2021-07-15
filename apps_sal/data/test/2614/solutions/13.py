# import sys; input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**7)
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	T = int(input())
	for _ in range(T):
		N = int(input())
		A = getlist()
		D = defaultdict(int)
		for i in A:
			D[i] += 1

		D2 = defaultdict(int)
		for i in D:
			D2[D[i]] += 1

		# print(D2)
		val = 0
		num = 0
		for i in D2:
			if i > val:
				val = i
				num = D2[i]

		# print(val, num)
		ans = int((N - num) // (val - 1)) - 1
		print(ans)


def __starting_point():
	main()
__starting_point()
