class Node:
    def __init__(self, v, i):
        self.v = v
        self.i = i
        self.left = None
        self.right = None


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nodes = [Node(v, i) for i, v in enumerate(nums)]
sort = [[v, i] for i, v in enumerate(nums)]
sort = sorted(sort, key=lambda x: [x[0], x[1]], reverse=True)
for i in range(len(nodes)):
    if i < len(nodes) - 1:
        nodes[i].right = nodes[i + 1]
    if i > 0:
        nodes[i].left = nodes[i - 1]
ans = [0] * n

team = 1
for pair in sort:
    v, i = pair

    # if nodes[i].left == None and nodes[i].right == None:
    #     continue
    if nodes[i].i == None:
        continue
    # print(v, i)
    ans[i] = team if team == 1 else 2
    cur = nodes[i].right
    right = None
    for j in range(k):
        if cur == None:
            break
        right = cur.right
        ans[cur.i] = team if team == 1 else 2
        cur.i = None
        cur = right
    cur = nodes[i].left
    # print(cur.i, cur.v)
    left = None
    for j in range(k):
        if cur == None:
            break
        left = cur.left
        ans[cur.i] = team if team == 1 else 2
        cur.i = None
        cur = left
    # if left == None and right == None:
    #     break
    if left:
        left.right = right
    if right:
        right.left = left
    team = team ^ 1

print(''.join([str(i) for i in ans]))
