n, k = map(int, input().split())
l = [*map(int, input().split())]
curr = res = 0
for i, e in enumerate(l):
    if i != 0 and l[i] == l[i - 1]:
        curr = i
    res = max(res, i - curr + 1)
print(res)
