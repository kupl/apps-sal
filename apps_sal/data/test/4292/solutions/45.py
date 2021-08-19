from itertools import accumulate
(N, K) = map(int, input().split())
P = [0] + list(accumulate(sorted(map(int, input().split()))))
print(P[K])
