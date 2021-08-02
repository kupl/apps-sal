import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

P_list = list(itertools.permutations(P, len(P)))
P_list.sort()
p = P_list.index(P)
q = P_list.index(Q)
print(abs(p - q))
