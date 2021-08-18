import sys
import itertools

A = list(map(int, input().split()))

ans = sys.maxsize
for A_1, A_2, A_3 in itertools.permutations(A, r=3):
    ans = min(ans, abs(A_2 - A_1) + abs(A_3 - A_2))

print(ans)
