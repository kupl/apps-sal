n = int(input())
ls = list(map(int, input().split()))

ls.sort()
res = set()
for elt in ls:
    if elt > 1 and elt - 1 not in res:
        res.add(elt - 1)
    elif elt not in res:
        res.add(elt)
    elif elt + 1 not in res:
        res.add(elt + 1)

print(len(res))
