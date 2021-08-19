from itertools import combinations
N = int(input())
D = list(map(int, input().split()))
ans = 0
for (i, j) in combinations(D, 2):
    ans += i * j
print(ans)
