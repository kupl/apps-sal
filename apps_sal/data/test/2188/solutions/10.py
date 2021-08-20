n = int(input())
p = [tuple((int(x) for x in input().split())) for _ in range(n)]
asc = [(x[0], i) for (i, x) in enumerate(p) if x[0] > x[1]]
desc = [(x[0], i) for (i, x) in enumerate(p) if x[0] < x[1]]
asc.sort()
desc.sort(reverse=True)
if len(asc) >= len(desc):
    print(len(asc))
    print(' '.join((str(x[1] + 1) for x in asc)))
else:
    print(len(desc))
    print(' '.join((str(x[1] + 1) for x in desc)))
