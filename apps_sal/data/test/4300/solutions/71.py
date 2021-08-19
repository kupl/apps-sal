from itertools import combinations
n = int(input())
d = list(map(int, input().split()))
ans = 0
d = combinations(d, 2)
for (i, j) in d:
    ans += i * j
print(ans)
