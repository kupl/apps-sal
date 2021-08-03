idx = []
size = []


def root(x):
    while x != idx[x]:
        # path compression start
        idx[x] = idx[idx[x]]
        # path compression end
        x = idx[x]
    return x


def connected(p, q):
    return root(p) == root(q)


def union(p, q):
    i = root(p)
    j = root(q)

    if size[i] < size[j]:
        idx[i] = j
        size[j] += size[i]
    else:
        idx[j] = i
        size[i] += size[j]


sa = input().split(' ')
chems = int(sa[0])
reacts = int(sa[1])
for t in range(chems):
    idx.append(t)

size = [1] * chems

for reaction in range(reacts):
    sa = input().split(' ')
    union(int(sa[0]) - 1, int(sa[1]) - 1)
for t in range(len(idx)):
    idx[t] = root(idx[t])
print(2**(chems - len(set(idx))))
