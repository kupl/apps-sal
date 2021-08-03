n, m = map(int, input().split())
G = [0] * n
parent = list(range(n))


def FindAncester(i):
    if i == parent[i]:
        pass
    else:
        parent[i] = FindAncester(parent[i])
    return parent[i]


def MergeTwo(i, j):
    A = FindAncester(i)
    B = FindAncester(j)
    parent[B] = parent[A]


for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if a > b:
        a, b = b, a
    G[a] += 1
    G[b] += 1
    MergeTwo(a, b)

R = {}
count = 0
for i in range(n):
    a = FindAncester(i)
    if a in R:
        R[a].append(i)
    else:
        R[a] = [i]
# print(parent)
# print(G)
for i in R:
    if len(R[i]) > 2:
        x = 1
        for j in R[i]:
            if G[j] != 2:
                x = 0
                break
        if x == 1:
            count += 1
print(count)
