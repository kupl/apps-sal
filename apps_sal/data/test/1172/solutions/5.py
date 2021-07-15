import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
	S = SI()
	N = len(S)
	dp = make_grid(N+1, 4, 0)
	dic = {"A": [0], "B": [1], "C": [2], "?": [0,1,2]}
	dp[0][0] = 1
	for i, s in enumerate(S):
		if s == "?":
			for j in range(4):
				if j in dic[s]:
					dp[i+1][j+1] += dp[i][j] % MOD
				dp[i+1][j] += dp[i][j] * 3 % MOD
		else:
			for j in range(4):
				if j in dic[s]:
					dp[i+1][j+1] += dp[i][j] % MOD

				dp[i+1][j] += dp[i][j] % MOD

	print(dp[N][3] % MOD)



def __starting_point():
	main()
__starting_point()
