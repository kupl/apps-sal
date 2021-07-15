pqr = list(map(int, input().split()))
from itertools import permutations
ans = 100*3
for i, j in permutations(pqr, 2):
    ans = min(ans, i+j)
print(ans)
