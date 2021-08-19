import collections
cols, pairs = [int(x) for x in input().split()]

d = collections.defaultdict(list)

for _ in range(pairs):
    a, b = [int(x) for x in input().split()]
    d[a].append(b)
    # d[b].append(a)

rooks = collections.defaultdict(list)
# rooks = [[] for _ in range(cols)]

current_line = 1
for i in range(1, cols + 1):

    rooks[i].append((i, current_line))
    current_line += 1

    for harmony in d[i]:
        rooks[i].append((i, current_line))
        rooks[harmony].append((harmony, current_line))
        current_line += 1

for i in range(1, cols + 1):
    print(len(rooks[i]))
    for a, b in rooks[i]:
        print(a, b)
