from itertools import combinations
(n, l, r, x) = map(int, input().split())
problems = [int(x) for x in input().split()]
ans = 0
for i in range(2, n + 1):
    for comb in combinations(problems, i):
        isum = sum(comb)
        imin = min(comb)
        imax = max(comb)
        if l <= isum <= r and imax - imin >= x:
            ans += 1
print(ans)
