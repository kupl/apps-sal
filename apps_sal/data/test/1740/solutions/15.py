n = int(input())


class Leader(object):
    def __init__(self, value):
        self.array = [value]


def union(v1, v2):
    leader = v1 if len(dsets[v1].array) >= len(dsets[v2].array) else v2
    antileader = v1 if leader == v2 else v2

    dsets[leader].array.extend(dsets[antileader].array)

    for v in dsets[antileader].array:
        dsets[v] = dsets[leader]


dsets = [Leader(i) for i in range(n)]

for _ in range(n - 1):
    v1, v2 = [int(t) - 1 for t in input().split(' ')]
    union(v1, v2)

print(' '.join(str(t + 1) for t in dsets[0].array))
