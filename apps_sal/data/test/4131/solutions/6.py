from collections import defaultdict

n, m = list(map(int, input().split()))
prefecture = [[] for _ in range(n+1)]
tpl_lst=[]
for i in range(m):
    p, y = list(map(int, input().split()))
    prefecture[p].append(y)
    tpl_lst.append((p,y))

for p in prefecture:
    if len(p)>=2:
        p.sort()

d = defaultdict(list)
for idx, pre in enumerate(prefecture):
    if len(pre)>=1:
        for i, year in enumerate(pre):
            d[(idx, year)]=[idx, i+1]

for tpl in tpl_lst:
    id = d[tpl][0]*(10**6) + d[tpl][1]
    id = str(id)
    id = "0"*(12-len(id)) + id
    print(id)
#print(prefecture)

