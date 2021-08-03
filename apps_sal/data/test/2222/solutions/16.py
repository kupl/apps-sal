n = int(input())
op = [int(g) for g in input().split()]
parent = [int(g) - 1 for g in input().split()]
tree = [[] for i in range(n)]
for i in range(n - 1):
    tree[parent[i]].append(i + 1)
l = sum([1 for i in range(n) if len(tree[i]) == 0])

l1 = [-1] * n
for i in range(n - 1, -1, -1):
    if len(tree[i]) == 0:
        l1[i] = 1
    else:
        x = [l1[j] for j in tree[i]]
        if op[i] == 1:
            l1[i] = min(x)
        else:
            l1[i] = sum(x)
print(l - l1[0] + 1)
