from itertools import *
(N, K) = map(int, input().split())
S = input()
A = []
for (i, j) in groupby(S):
    A += [len(list(j)) - 1]
print(min(N - 1, sum(A) + 2 * K))
