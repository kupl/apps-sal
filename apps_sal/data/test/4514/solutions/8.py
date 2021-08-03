from collections import deque as dq
from collections import defaultdict as dc


def dfs(stack, vis, child, when, ab):
    while(len(stack) > 0):
        a = stack[-1]
        if vis[a] == 1:
            child[a] = len(ab) - when[a]
            c = stack.pop()
            continue
        ab.append(a)
        when[a] = len(ab) - 1
        # print(a)
        vis[a] = 1
        for i in reversed(adj[a]):
            stack.append(i)


            # print(stack)
adj = dc(list)
n, q = list(map(int, input().split()))
child = [0] * (n + 1)  # store the max no. of sub tree element
when = [0] * (n + 1)  # store i element is at when[i] place in ab
ab = []  # the dfs element
vis = [0] * (n + 1)
stack = dq([1])
a = list(map(int, input().split()))
for i in range(2, n + 1):
    adj[a[i - 2]].append(i)
dfs(stack, vis, child, when, ab)
# print(child)
z = []
for i in range(q):
    x, y = list(map(int, input().split()))
    y = y - 1
    if y >= child[x]:
        z.append(str(-1))
    else:
        z.append(str(ab[when[x] + y]))
print('\n'.join(z))
