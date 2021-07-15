import sys
sys.setrecursionlimit(10000)


def painting_fence(fence, cut):
	n = len(fence)
	if n == 0: return 0
	min_i = fence.index(min(fence))
	min_h = fence[min_i]
	ans = min_h-cut+painting_fence(fence[:min_i], min_h)+painting_fence(fence[min_i + 1:], min_h)
	return min(ans, n)

def main():
	_ = int(input())
	fence = list(map(int, input().split()))
	print(painting_fence(fence, 0))

def __starting_point():
	main()
__starting_point()
