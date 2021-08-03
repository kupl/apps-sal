from collections import deque


mod = 10 ** 9 + 7
SIZE = 2 * 10 ** 5 + 1
fact = [0] * SIZE
inv = [0] * SIZE
finv = [0] * SIZE
fact[0], fact[1] = 1, 1
inv[1] = 1
finv[0], finv[1] = 1, 1
for i in range(2, SIZE):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def nCr(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    return fact[n] * (finv[r] * finv[n - r] % mod) % mod


n = int(input())
edges = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

root_to_leaf = []
parents = [0] * n

todo = deque([])
for to in edges[0]:
    todo.append([to, 0])

while todo:
    node, parent = todo.popleft()
    root_to_leaf.append(node)
    parents[node] = parent

    for to in edges[node]:
        if to == parent:
            continue
        todo.append([to, node])

size_of_subtree = [0] * n
pattern_in_subtree = [1] * n

for node in root_to_leaf[::-1]:
    parent = parents[node]
    size_of_subtree[node] += 1
    size_of_subtree[parent] += size_of_subtree[node]
    pattern_in_subtree[parent] *= nCr(size_of_subtree[parent], size_of_subtree[node]) * pattern_in_subtree[node] % mod
    pattern_in_subtree[parent] %= mod

answers = [0] * n
answers[0] = pattern_in_subtree[0]

for node in root_to_leaf:
    parent = parents[node]
    ans = answers[parent] * size_of_subtree[node] * inv[n - size_of_subtree[node]] % mod
    answers[node] = ans

for ans in answers:
    print(ans)
