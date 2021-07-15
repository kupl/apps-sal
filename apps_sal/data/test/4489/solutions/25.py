N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

from collections import Counter
counter = Counter(S)
counter.subtract(T)
print(max(0, max(counter.values())))
