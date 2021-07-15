from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for x in a:
    d[min(x//400, 8)] += 1
mi = len(d.keys())
if d[8] > 0 and mi >= 2:
    mi -= 1
mx = d[8]+len([i for i in range(8) if i in d])
print(mi, mx)
