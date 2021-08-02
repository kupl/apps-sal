import collections
_, A = open(0); P, Q = map(collections.Counter, zip(*[[i - a, i + a]for i, a in enumerate(map(int, A.split()))])); print(sum(P[i] * Q[i]for i in range(6**7)))
