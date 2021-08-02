import itertools
n, l, r, x = list(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = 0
if len(C) > 1:
    for i in range(2, len(C) + 1):
        for j in itertools.combinations(C, i):
            if l <= sum(j) <= r and max(j) - min(j) >= x: ans += 1

print(ans)
