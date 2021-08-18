from collections import Counter


nodes_nr = int(input())
node_idx___neigh_idxes = []
for _ in range(nodes_nr):
    node_idx___neigh_idxes.append([])
for _ in range(nodes_nr - 1):
    node_idx1, node_idx2 = (int(x) - 1 for x in input().split())
    node_idx___neigh_idxes[node_idx1].append(node_idx2)
    node_idx___neigh_idxes[node_idx2].append(node_idx1)

node_idx___group = [-1] * nodes_nr
stack = []
stack.append(0)
node_idx___group[0] = 0

while stack:
    curr_node_idx = stack.pop()
    for neigh_idx in node_idx___neigh_idxes[curr_node_idx]:
        if node_idx___group[neigh_idx] == -1:
            if node_idx___group[curr_node_idx] == 0:
                node_idx___group[neigh_idx] = 1
            else:
                node_idx___group[neigh_idx] = 0
            stack.append(neigh_idx)

counter = Counter(node_idx___group)
ans = counter[0] * counter[1] - nodes_nr + 1
print(ans)
