def find(node):
    while p[node] != node:
        p[node] = p[p[node]]
        node = p[node]
    return node


def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if p1 != p2:
        p[p1] = p2


n, m, k = map(int, input().split())
socks = list(map(int, input().split()))
p = [i for i in range(n)]
used = set()
for i in range(m):
    a, b = map(int, input().split())

    union(a - 1, b - 1)
    used.add(a - 1)
    used.add(b - 1)
cc = {}

for i in used:
    x = find(i)
    if x not in cc:
        cc[x] = []
        cc[x].append(socks[i])
    else:
        cc[x].append(socks[i])
ans = 0
for each in cc.values():
    each.sort()
    cnt = 1
    l = len(each)
    mx = 1
    for i in range(l - 1):
        if each[i + 1] != each[i]:
            mx = max(mx, cnt)
            cnt = 1
        else:
            cnt += 1
    mx = max(cnt, mx)
    ans += l - mx
print(ans)
