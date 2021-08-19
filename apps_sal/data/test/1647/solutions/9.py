from collections import defaultdict


length = int(input().strip())
s1 = input().strip()
s2 = input().strip()

adj = defaultdict(list)
nodes = set()

for c1, c2 in zip(s1, s2):
    if c1 != c2:  # add to undirected graph
        adj[c1].append(c2)
        adj[c2].append(c1)
        nodes.add(c1)
        nodes.add(c2)

v = set()
st = []


def dfs(n):
    v.add(n)
    for neighbor in adj[n]:
        if neighbor not in v:
            st.append((n, neighbor))
            dfs(neighbor)


for n in nodes:
    if n not in v:
        dfs(n)

print(len(st))
for pair in st:
    print(*pair)
