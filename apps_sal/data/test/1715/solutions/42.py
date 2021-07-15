import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
	A, B, Q = NMI()
	S = [-float("inf")] + [NI() for _ in range(A)] + [float("inf")]
	T = [-float("inf")] + [NI() for _ in range(B)] + [float("inf")]
	Q = [NI() for _ in range(Q)]

	for q in Q:
		s_idx = bisect.bisect_left(S, q)
		t_idx = bisect.bisect_left(T, q)
		sl, sr, tl, tr = S[s_idx-1], S[s_idx], T[t_idx-1], T[t_idx]
		LL = max(abs(q - sl), abs(q - tl))
		RR = max(abs(q - sr), abs(q - tr))
		LR = abs(q - sl) * 2 + abs(q - tr)
		RL = abs(q - sr) * 2 + abs(q - tl)
		LR2 = abs(q - tl) * 2 + abs(q - sr)
		RL2 = abs(q - tr) * 2 + abs(q - sl)
		res = min(LL, RR, LR, LR2, RL, RL2)
		print(res)


def __starting_point():
	main()
__starting_point()
