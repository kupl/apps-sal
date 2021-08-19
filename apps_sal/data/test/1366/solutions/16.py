from collections import defaultdict as ddict
N = int(input())
count = ddict(int)
bottles = []
for i in range(N):
    (ai, bi) = map(int, input().split())
    count[bi] += 1
    bottles.append((ai, bi))
res = 0
for (ai, bi) in bottles:
    if count[ai] == 0 or (count[ai] == 1 and bi == ai):
        res += 1
print(res)
