import sys

n = int(input())
minmax = list(map(int, input().split()))
childs = [[] for i in range(n)]

for idx, father in enumerate(list(map(int, input().split()))):
    childs[father - 1].append(idx + 1)

stack = []
stack.append(0)

ans = [None for ele in range(n)]
vis = [False for ele in range(n)]

while len(stack):
    index = stack[-1]
    if not vis[index]:
        vis[index] = True
        if len(childs[index]) == 0:
            ans[index] = (0, 1)
            stack.pop()
        else:
            for child in childs[index]:
                stack.append(child)
    else:
        stack.pop()
        res = [ans[child] for child in childs[index]]
        total = sum([ele[1] for ele in res])
        if minmax[index] == 1:
            ans[index] = min([ele[0] for ele in res]), total
        else:
            bigger_than = sum([ele[1] - ele[0] - 1 for ele in res])
            ans[index] = total - bigger_than - 1, total

print(ans[0][1] - ans[0][0])
