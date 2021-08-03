import itertools
l, r = map(int, input().split())
if r - l >= 2019:
    print(0)
    return
w = []
q = list(itertools.combinations(range(l, r + 1), 2))
for i in range(len(q)):
    w.append((q[i][0] * q[i][1]) % 2019)

print(min(w))
