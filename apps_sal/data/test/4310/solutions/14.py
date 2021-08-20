from itertools import permutations
A = list(map(int, input().split()))
per_ls = list(permutations(A))
ans = float('inf')
for (a, b, c) in per_ls:
    tmp = 0 + abs(a - b) + abs(b - c)
    ans = min(ans, tmp)
print(ans)
