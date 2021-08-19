n = int(input())
a = [int(x) for x in input().split()]
m = min(a)
mdist = 0
(fst, l) = (None, None)
for i in [i for (i, x) in enumerate(a) if x == m]:
    if fst is None:
        fst = l = i
    else:
        mdist = max(mdist, i - l - 1)
        l = i
mdist = max(mdist, fst + (n - l) - 1)
print(n * m + mdist)
