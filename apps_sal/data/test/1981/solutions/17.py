from collections import defaultdict
from collections import namedtuple
State = namedtuple('State', ['node', 'remain', 'parent'])
(n, m) = [int(x) for x in input().split()]
cats = [int(x) for x in input().split()]
graph = defaultdict(set)
for _ in range(n - 1):
    (i, j) = [int(x) - 1 for x in input().split()]
    graph[i].add(j)
    graph[j].add(i)
ans = 0
stack = [State(0, m, None)]
while stack:
    st = stack.pop()
    rem = st.remain - 1 if cats[st.node] else m
    if rem >= 0:
        num_of_children = 0
        for child in graph[st.node]:
            if child != st.parent:
                stack.append(State(child, rem, st.node))
                num_of_children += 1
        if num_of_children == 0:
            ans += 1
print(ans)
