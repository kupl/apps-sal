import sys
from itertools import product
(N, M) = map(int, sys.stdin.readline().rstrip().split())
cake = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0
for (i, j, k) in product([-1, 1], repeat=3):
    data = [i * x + j * y + k * z for (x, y, z) in cake]
    ans = max(ans, sum(sorted(data)[::-1][:M]))
print(ans)
