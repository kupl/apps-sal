n = int(input())
our = list(map(int, input().split()))
tab = set()
res = 0
for elem in our:
    if elem in tab:
        tab.discard(elem)
    else:
        tab.add(elem)
    res = max(res, len(tab))
print(res)
