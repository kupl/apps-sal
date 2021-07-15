import itertools
import copy
n = int(input())
P = list(map(int, input().split()))
Q = tuple(list(map(int, input().split())))
P_ = copy.copy(P)
P_.sort()
p_list = list(itertools.permutations(P_))
P = tuple(P)

a = p_list.index(P)
b = p_list.index(Q)

print(abs(a-b))
