import sys


class node:

    def __init__(self, value, parent, respect):
        self.value = value
        self.children = []
        self.parent = parent
        self.respect = respect


all_nodes = {}
root = -1
not_respectors = []
n = int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline()[:-1]
    (node_parent, node_res) = line.split(' ')
    if i + 1 in all_nodes:
        all_nodes[i + 1].parent = int(node_parent)
        all_nodes[i + 1].respect = int(node_res)
    else:
        all_nodes[i + 1] = node(i + 1, int(node_parent), int(node_res))
    if int(node_parent) == -1:
        root = all_nodes[i + 1]
    else:
        int_node_parent = int(node_parent)
        if int_node_parent not in all_nodes:
            all_nodes[int_node_parent] = node(int_node_parent, -1, -1)
        all_nodes[int_node_parent].children.append(all_nodes[i + 1])
    if int(node_res) == 1:
        not_respectors.append(all_nodes[i + 1])


def get_val(n):
    return n.value


not_respecters = sorted(not_respectors, key=get_val)
tot = []
for n in not_respectors:
    b = True
    for c in n.children:
        if c.respect == 0:
            b = False
            break
    if b:
        tot.append(n)
if len(tot) == 0:
    print('-1')
else:
    print(' '.join(map(str, list(map(get_val, tot)))))
