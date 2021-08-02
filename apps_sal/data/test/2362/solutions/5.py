from math import gcd
n = int(input())
a = [int(i) for i in input().split()]
tree = [[] for i in range(0, n)]

for i in range(0, n - 1):
    s = input().split()
    v1 = int(s[0]) - 1
    v2 = int(s[1]) - 1
    tree[v1].append(v2)
    tree[v2].append(v1)

ans = 0
d = [{} for i in range(0, n)]
for i in range(0, n):
    d[i] = {a[i]: 1}  # gcd to path_length
    if a[i] > 1:
        ans = 1


def dfs(curr, parent):
    for child in tree[curr]:
        if child == parent:
            continue
        dfs(child, curr)

        new_gcd = gcd(a[curr], a[child])
        if new_gcd > 1:
            for g_parent, p_parent in list(d[curr].items()):
                for g_child, p_child in list(d[child].items()):
                    if gcd(g_parent, g_child) > 1:
                        nonlocal ans
                        ans = max(ans, p_parent + p_child)

        for g_child, p_child in list(d[child].items()):
            new_gcd = gcd(a[curr], g_child)
            if new_gcd > 1:
                if new_gcd in d[curr]:
                    d[curr][new_gcd] = max(d[curr][new_gcd], p_child + 1)
                else:
                    d[curr][new_gcd] = p_child + 1


dfs(0, -1)
print(ans)
