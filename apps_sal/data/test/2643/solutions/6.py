import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
printV = lambda x: print(*x, sep="\n")
printH = lambda x: print(" ".join(map(str,x)))
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	k,q = MI()
	d = LI()
	d = np.array(d)
	ans = [0]*q
	for i in range(q):
		n,x,m = MI()
		d_modm = d%m
		zero = ((n-1)//k)*np.sum(d_modm==0) + np.sum((d_modm==0)[:(n-1)%k])
		last = x + ((n-1)//k)*np.sum(d_modm) + np.sum((d_modm)[:(n-1)%k])
		ans[i]=(n-1)-zero-(last//m-x//m)
	printV(ans)

def __starting_point():
	main()
__starting_point()
