import sys
import re
import queue
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []



def main():
	N = i_input()

	x_y_list = []

	for i in range(0,N):
		tmpx,tmpy = i_map()
		x_y_list.append((tmpx,tmpy))

	z_list = []
	w_list = []
	for i in range(0,N):
		tmpz = x_y_list[i][0] + x_y_list[i][1]
		tmpw = x_y_list[i][0] - x_y_list[i][1]
		z_list.append(tmpz)
		w_list.append(tmpw)

	print(max(max(map(lambda x : (x),z_list))-min(map(lambda x: (x), z_list)),max(map(lambda x : (x),w_list))-min(map(lambda x: (x),w_list))))
	
	return


def __starting_point():
	main()
__starting_point()
