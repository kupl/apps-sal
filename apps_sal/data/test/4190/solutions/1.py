n = int(input())
a = map(int, input().split())
b = map(int, input().split())
(parent, rank) = ([-1] * n, [0] * n)
source = [i for i in range(n)]
occurences = [0] * n
printer = []


def fp(x):
    stack = []
    curr = x
    while parent[curr] != -1:
        stack.append(curr)
        curr = parent[curr]
    for v in stack:
        parent[v] = curr
    return curr


def u(x, y):
    best = None
    (xP, yP) = (fp(x), fp(y))
    if rank[x] < rank[y]:
        best = parent[xP] = yP
    elif rank[x] > rank[y]:
        best = parent[yP] = xP
    else:
        best = parent[yP] = xP
        rank[xP] += 1
    if occurences[source[best]] == 0:
        source[best] = source[xP] if yP is best else source[yP]


for x in b:
    occurences[x] += 1
for i in range(n):
    if occurences[i] == 0:
        u(i, (i + 1) % n)
for val in a:
    p = source[fp((n - val) % n)]
    printer.append(str((val + p) % n))
    occurences[p] -= 1
    if occurences[p] == 0:
        u(p, (p + 1) % n)
print(' '.join(printer))
