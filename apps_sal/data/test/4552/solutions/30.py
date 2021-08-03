from itertools import product
n = int(input())
fs = [list(map(int, input().split())) for _ in range(n)]
ps = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')
for b in product((0, 1), repeat=10):
    if sum(b) == 0:
        continue
    v = 0
    for f, p in zip(fs, ps):
        cnt = sum([a & b for a, b in zip(b, f)])
        v += p[cnt]
    ans = max(ans, v)
print(ans)
