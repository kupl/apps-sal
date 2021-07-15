import itertools
n = int(input())
d = list(map(int, input().split()))
M = []
ans = 0

for v in itertools.combinations(d, 2):
    M.append(list(v))

for m in M:
    ans += m[0]*m[1]
print(ans)
