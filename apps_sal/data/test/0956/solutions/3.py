import sys
from collections import defaultdict

m, k = list(map(int, sys.stdin.readline().split()))
f = defaultdict(list)
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    f[a].append(b)
    f[b].append(a)

for i, list_a in sorted(f.items()):
    all_f = set(list_a)
    total_f = len(all_f)
    sugg = []
    for j, list_b in list(f.items()):
        if j == i or j in all_f:
            continue
        common_f = set()
        for p in list_b:
            if p in all_f:
                common_f.add(p)
        if len(common_f) * 100 >= k * total_f:
            sugg.append(j)
    sys.stdout.write('%d: %d %s\n' % (
        i,
        len(sugg),
        ' '.join(map(str, sorted(sugg)))
    ))

