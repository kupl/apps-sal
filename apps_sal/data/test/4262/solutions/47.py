import itertools
import math
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
l = [x for x in range(1, N + 1)]
lst = list(itertools.permutations(l))
print(abs(lst.index(P) - lst.index(Q)))
