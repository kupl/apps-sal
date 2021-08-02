n, l, r, x = list(map(int, input().split()))
cs = list(map(int, input().split()))


def subsets(x):
    if len(x) == 0:
        return [[]]
    a = subsets(x[1:])
    b = [[x[0]] + c for c in a]
    return a + b


sets = subsets(cs)

ans = 0
for s in sets:
    if len(s) < 2:
        continue
    if not (l <= sum(s) <= r):
        continue
    if max(s) - min(s) < x:
        continue
    ans += 1
print(ans)
