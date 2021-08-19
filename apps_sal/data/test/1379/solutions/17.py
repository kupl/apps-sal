(n, m, D) = map(int, input().split())
lst = [*map(int, input().split())]
d = {}
for (i, x) in enumerate(lst):
    d[x] = i
lst.sort()
(res, j, result) = ([0] * n, 0, 0)
for (i, x) in enumerate(lst):
    if x - lst[j] > D:
        res[d[x]] = res[d[lst[j]]]
        j += 1
    else:
        result += 1
        res[d[x]] = result
print(result)
print(*res)
