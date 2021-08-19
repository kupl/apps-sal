(n, s) = list(map(int, input().split()))
tree = [[] for i in range(n)]
for i in range(n - 1):
    inp = list([int(x) - 1 for x in input().split()])
    tree[inp[0]].append(inp[1])
    tree[inp[1]].append(inp[0])
cou = 0
for i in tree:
    if len(i) == 1:
        cou += 1
print(s / cou * 2)
