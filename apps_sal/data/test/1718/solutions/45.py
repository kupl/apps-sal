import sys
import math
import collections
input = sys.stdin.readline
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = math.ceil((N - 1) / (K - 1))
print(ans)
