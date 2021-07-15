from collections import defaultdict

def subs(s):
    for l in range(1, len(s) + 1):
        for shift in range(0, len(s) - l + 1):
            yield s[shift : shift + l]

n = int(input())
vs = [input() for _ in range(n)]

entries = defaultdict(set)
for i, s in enumerate(vs):
    for sub in subs(s):
        entries[sub].add(i)

for s in vs:
    for sub in subs(s):
        if len(entries[sub]) == 1:
            print(sub)
            break

