# import sys; input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**7)
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def inverse(N, mod):
	return (pow(N, mod - 2, mod))

def main():
	S = list(input())
	N = len(S)
	print(3)
	print("L", N - 1)
	print("R", N - 1)
	print("R", 2 * N - 1)
	# s = S
	# s = s[1:N - 1][::-1] + s
	# print("".join(s))
	# s = s + s[N - 1:2* N - 3][::-1]
	# print("".join(s))
	# s = s + s[2 * N - 1:3 * N - 4][::-1]
	# print("".join(s))


def __starting_point():
	main()
__starting_point()
