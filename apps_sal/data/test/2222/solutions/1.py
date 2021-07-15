from collections import defaultdict
from collections import deque
# import sys
# sys.setrecursionlimit(400000)
n = int(input())
tree = defaultdict(set)
node_type = list(map(int,input().split()))
#leaf = [True for x in range(n)]
values = [0 for x in range(n)]
for i,x in enumerate(map(int,input().split())):
    tree[x-1].add(i+1)
    #leaf[x-1] = False

queue = deque([(0,False)])
while queue:
    node, tag = queue.popleft()
    if not node in tree:
        values[node] = 1
        continue
    elif tag:
        if node_type[node]:
            values[node] = min(values[c] for c in tree[node])
        else:
            values[node] = sum(values[c] for c in tree[node])
    else:
        queue.appendleft((node,True))
        queue.extendleft((c,False) for c in tree[node])
#print(values)
k = n-len(tree)
print (k-values[0]+1)
