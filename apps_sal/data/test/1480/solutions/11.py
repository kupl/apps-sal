(n, k) = map(int, input().split())
a = list(map(int, input().split()))


def round(children, a, leader):
    lead_pos = children.index(leader)
    a = (lead_pos + a) % len(children)
    deleted = children[a]
    del children[a]
    return (children, a % len(children), deleted)


children = list(range(1, n + 1))
result = []
leader = 1
for i in range(k):
    (children, leader_pos, deleted) = round(children, a[i], leader)
    leader = children[leader_pos]
    result.append(deleted)
print(*result, sep=' ')
