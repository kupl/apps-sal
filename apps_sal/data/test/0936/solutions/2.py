n = input()
has = {}
best = -1
has[best] = -1
ar = [int(x) for x in input().split()]
for x in ar:
    if x not in has:
        has[x] = 1
    else:
        has[x] += 1
    if has[x] > has[best]:
        best = x
print(best)
