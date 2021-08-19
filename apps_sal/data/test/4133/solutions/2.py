import re

line = input()

line = line.rstrip('.')
a, b, c = line.partition("):-")
rels = c.split(',')

relations = set()
for rel in rels:
    if "<" in rel:
        x, _, y = rel.partition("<")
        relations.add((len(x), len(y)))
    else:
        x, _, y = rel.partition(">")
        relations.add((len(y), len(x)))

a = a.lstrip("?(")
args = re.split(r"(\+|-|\*|/)", a)
args = [len(args[i]) for i in range(0, len(args), 2)]


# print(args)
# print(relations)

edges = {k: [] for k in args}
for j, i in relations:
    edges[i].append(j)

seen = {k: 0 for k in args}

q = []


def topsort(k):
    if seen[k] == 1:
        print("false")
        quit()
    seen[k] = 1
    for other in edges[k]:
        topsort(other)
    q.append(k)
    seen[k] = 2
    return True


for k in args:
    if seen[k] == 0:
        topsort(k)

vals = {}

for k in q:
    others = edges[k]
    maxval = -1
    for other in others:
        maxval = max(maxval, vals.get(other, -1))
    vals[k] = maxval + 1
    if(vals[k] > 9):
        print("false")
        quit()

for k in args:
    print(vals[k], end='')

print()
