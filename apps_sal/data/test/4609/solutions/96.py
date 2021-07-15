
from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

L = Counter(A)

print(sum( 1 for c in L.values() if c%2 ))
