import sys
def input(): return sys.stdin.readline().rstrip()


def inpl(): return list(map(int, input().split()))


N, M = inpl()
uv = [set() for _ in range(N)]
vu = [set() for _ in range(N)]
for _ in range(M):
    A, B = inpl()
    uv[A - 1].add(B - 1)
    vu[B - 1].add(A - 1)

EMPTY, LOOP, TREE = 0, 1, 2
ENTER, EXIT = 0, 1
status = [EMPTY] * N
for s in range(N):
    states_pool = [(s, [], ENTER)]
    while states_pool:
        u, chain, flag = states_pool.pop()
        if flag == EXIT or status[u] == TREE:
            status[u] = TREE
            continue
        elif status[u] == LOOP:
            break
        else:  # ENTER, EMPTY
            status[u] = LOOP
            states_pool.append((u, chain, EXIT))
            new_chain = chain.copy()
            new_chain.append(u)
            for c in uv[u]:
                states_pool.append((c, new_chain, ENTER))
    else:
        continue
    break
else:
    print(-1)
    return

n = 0
while chain[n] != u:
    n += 1
chain = chain[n:]
L = len(chain)
nextnode = [None] * N
for i in range(L - 1):
    nextnode[chain[i]] = chain[i + 1]
nextnode[chain[L - 1]] = chain[0]
pos = [None] * N
for p in range(len(chain)):
    pos[chain[p]] = p
i = 0
while i < L:
    h = 1
    c = chain[(i + 1) % L]
    for j in uv[chain[i % L]]:
        p = pos[j]
        if p is None:
            continue
        else:
            if (p - i) % L > h:
                h = (p - i) % L
                c = j
    nextnode[chain[i % L]] = c
    i += 1
    while chain[i % L] != c:
        pos[chain[i % L]] = None
        i += 1

loop = [c]
k = c
while nextnode[k] != c:
    k = nextnode[k]
    loop.append(k)
print(len(loop))
for l in loop:
    print(l + 1)
