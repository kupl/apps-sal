import itertools
n, l, r, var = (int(x) for x in input().split())
arr = list(int(x) for x in input().split())
ans = 0
for i in range(2, len(arr) + 1):
    for comb in itertools.combinations(arr, i):
        curComb = list(comb)
        if sum(curComb) <= r and sum(curComb) >= l and max(curComb) - min(curComb) >= var:
            ans += 1
print(ans)
