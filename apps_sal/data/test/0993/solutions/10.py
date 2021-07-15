import sys
import math
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
	N, M = NMI()
	A = NLI()
	C = make_cumulative(A)
	C = [c%M for c in C]
	C = Counter(C)
	ans = 0
	for c, x in C.items():
		if x >= 2:
			ans += x * (x-1) // 2
	print(ans)
	

def __starting_point():
	main()
__starting_point()
