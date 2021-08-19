n = int(input())
ls = list(map(int, input().split()))
ls.sort()
minh = set()
maxh = set()
for e in ls:
    if e - 1 not in maxh:
        maxh.add(e - 1)
    elif e not in maxh:
        maxh.add(e)
    else:
        maxh.add(e + 1)
    if e - 1 not in minh and e not in minh and (e + 1 not in minh):
        minh.add(e + 1)
print(len(minh), len(maxh))
