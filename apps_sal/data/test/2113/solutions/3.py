# Махмуд и Ехаб продолжают свои приключения! Каждый житель Злой Страны знает, что Доктор Зло любит двудольные графы, особенно деревья.
#
# Дерево — это связный граф без циклов. Двудольный граф — это граф, вершины которого можно разбить на 2 множества таким образом, что для любого ребра (u, v) графа вершины u и v лежат в разных множествах. Более формальное определение дерева и двудольного графа дано ниже.
#
# Доктор Зло дал Махмуду и Ехабу дерево, состоящее из n рёбер и сказал добавлять рёбра таким образом, чтобы граф оставался двудольным, а также в нём не было петель и кратных рёбер. Какое максимальное число рёбер они могут добавить?
# Входные данные
#
# В первой строке дано целое число n — число вершин в дереве (1 ≤ n ≤ 105).
#
# В следующих n - 1 строках содержатся пары целых чисел u и v (1 ≤ u, v ≤ n, u ≠ v) — описание рёбер дерева.
#
# Гарантируется, что заданный граф является деревом.
# Выходные данные
#
# Выведите одно число — максимальное число рёбер, которые Махмуд и Ехаб могут добавить в граф.
# python3
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
