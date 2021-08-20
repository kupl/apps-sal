n = int(input())
tree = {}
for i in range(n - 1):
    (_from, _to, cost) = map(int, input().split())
    if _from not in tree:
        tree[_from] = [(_to, cost)]
    else:
        tree[_from].append((_to, cost))
    if _to not in tree:
        tree[_to] = [(_from, cost)]
    else:
        tree[_to].append((_from, cost))
passed = [0] * n
all_cost = []


def compute_cost(node, cost):
    passed[node] = 1
    if len(tree[node]) != 0:
        for subnode in tree[node]:
            if passed[subnode[0]] != 1:
                all_cost.append(cost + subnode[1])
                compute_cost(subnode[0], cost + subnode[1])


compute_cost(0, 0)
print(max(all_cost))
